import os
import glob
from django.test import TestCase, TransactionTestCase
from django.core.files import File
from django.core.exceptions import ImproperlyConfigured
from django.core.urlresolvers import reverse
from django.test.client import Client
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from .models import Graffiti, validate_image
from .views import IndexGraffitiList
from .forms import AddGraffitiForm
from graffiti_map.settings import get_env_setting, MEDIA_ROOT


class EnvTestCase(TestCase):
    "Тест проверяющий функцию, возвращающую переменные окружения"

    def setUp(self):
        self.vars = ('SECRET_KEY', 'DB_NAME', 'DB_USER', 'DB_PASSWORD',
                     'DB_HOST', 'DB_PORT', 'RECAPTCHA_PUBLIC_KEY',
                     'RECAPTCHA_PRIVATE_KEY', 'MANDRILL_API_KEY', 'ADMIN_URL',
                     'THUMBNAIL_REDIS_HOST', 'THUMBNAIL_REDIS_PORT',
                     'THUMBNAIL_REDIS_DB', 'THUMBNAIL_REDIS_PASSWORD',
                     'SESSION_REDIS_HOST', 'SESSION_REDIS_PORT',
                     'SESSION_REDIS_DB', 'SESSION_REDIS_PASSWORD',
                     'SESSION_REDIS_PREFIX', 'SERVER_IP')

    def test_all_vars(self):
        for var in self.vars:
            self.failIf(var not in os.environ.keys(), 'Не задан %s' % var)

    def test_result(self):
        for var in self.vars:
            self.assertEqual(
                get_env_setting(var), os.environ[var], 'Проблема с %s' % var)

    def test_undeclared_var(self):
        # Исключение вызвано при обращении к несуществующей переменной окружения
        self.assertRaises(ImproperlyConfigured, get_env_setting, 'LOL')


class GraffitiTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        # можете написать с mock, BytesIO, StringIO и тд
        file = File(open('graffities/static/img/logo.jpg', 'rb'))
        cls.data = Graffiti.objects.create(id=1,
                                           photo=file,
                                           name='Тестовое граффити',
                                           comment='Тестовый коммент',
                                           lat=55.753559,
                                           lon=37.609218,
                                           checked=True)

    def setUp(self):
        self.client = Client()
        self.file_name = '%s/%s' % (MEDIA_ROOT,
                                    str(GraffitiTestCase.data.photo))
        self.file_generator = glob.iglob(self.file_name)

    def test_creation(self):
        graffiti = Graffiti.objects.get(name='Тестовое граффити')
        self.assertEqual(str(graffiti), '1, Тестовое граффити')

    def test_validator(self):
        self.assertRaises(ValidationError, validate_image, 'lol.png')

    def test_creation_in_fs(self):
        "проверяем, сохранилось ли фото в ФС"
        # если генератор не пуст, значит, что все ок. вероятность одинаковых имен файлов очень мала
        self.assertEqual(
            next(self.file_generator), self.file_name,
            'Имена файлов не совпадают')
        # при слудующем next() должна быть вызвана ошибка, ведь элемент в генераторе один
        self.assertRaises(StopIteration, next, self.file_generator)

    def test_index(self):
        response = self.client.get(reverse('index'))
        # Проверяем количество граффити на главной
        self.assertEqual(
            len(response.context['graffities']), 1,
            'Должно быть одно граффити')

    def test_graffiti_page(self):
        # не больше одного запроса
        with self.assertNumQueries(1):
            response = self.client.get(reverse('graffiti', args=[1]))
        self.assertEqual(response.status_code, 200,
                         'Ошибка при запросе страницы граффити')
        self.assertEqual('graffiti' in response.context.keys(), True,
                         'Должно быть граффити')

    def test_deletion(self):
        # не должно быть файлов и тд
        GraffitiTestCase.data.delete()
        # Поскольку файл удалили, то генератор должен быть пуст
        self.assertRaises(StopIteration, next, self.file_generator)

    def tearDown(self):
        # тут можно было бы удалить файл, который создали, но есть test_deletion()
        pass


class IndexPageTest(TransactionTestCase):
    def setUp(self):
        self.client = Client()

    def test_num_querises(self):
        with self.assertNumQueries(2):
            response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200,
                         'Ошибка при запросе главной')

    def test_post_method(self):
        # можно еще put patch и тд
        response = self.client.post(reverse('index'))
        self.assertEqual(response.status_code, 405,
                         'POST на главной не разрешен')


class GraffitiAdd(TestCase):
    def setUp(self):
        os.environ['RECAPTCHA_TESTING'] = 'True'
        self.client = Client()
        self.post_dict = {
            'name': 'Test',
            'comment': 'Test comment',
            'lat': 55.753559,
            'lon': 37.609218,
            'g-recaptcha-response': 'PASSED'
        }

    def test_form(self):
        # можно и сгенерить строку
        upload_file = open('graffities/static/img/logo.jpg', 'rb')
        file_dict = {
            'photo': SimpleUploadedFile(upload_file.name, upload_file.read())
        }
        form = AddGraffitiForm(self.post_dict, file_dict)
        self.assertEqual(form.is_valid(), True,
                         'Чего-то не так в форме добавления граффити')

    def test_post(self):
        with open('graffities/static/img/logo.jpg') as fp:
            response = self.client.post(
                reverse('add_graffiti'), self.post_dict.update({'photo': fp}))
        # не проверяем наличие тех или иных полей формы, так как сделали это выше
        self.assertEqual(response.status_code, 200,
                         'Проблема с публикацией граффити')

    def tearDown(self):
        os.environ['RECAPTCHA_TESTING'] = 'False'
