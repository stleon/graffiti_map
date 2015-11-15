from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from rest_framework import viewsets
from .models import Graffiti
from .forms import AddGraffitiForm
from .serializers import GraffitiSerializer


class IndexGraffitiList(ListView):
    template_name = 'index.html'
    queryset = Graffiti.objects.filter(
        active=True,
        checked=True).order_by('date_created').reverse()
    context_object_name = 'graffities'
    page_kwarg = 'str'
    paginate_by = 15

    @method_decorator(require_http_methods(["GET", ]))
    def dispatch(self, *args, **kwargs):
        return super(IndexGraffitiList, self).dispatch(*args, **kwargs)


class GraffitiDetail(DetailView):
    template_name = 'graffiti.html'
    context_object_name = 'graffiti'
    model = Graffiti

    @method_decorator(require_http_methods(["GET", ]))
    def dispatch(self, *args, **kwargs):
        return super(GraffitiDetail, self).dispatch(*args, **kwargs)


class GraffitiCreateView(CreateView):
    template_name = 'add_graffiti.html'
    model = Graffiti
    form_class = AddGraffitiForm

    def get_success_url(self):
        return reverse('success')

    def form_valid(self, form):
        # Оповещаем модераторов о том, что опубликовано новое граффити
        form.send_email()
        return super(GraffitiCreateView, self).form_valid(form)

    @method_decorator(require_http_methods(["GET", "POST"]))
    def dispatch(self, *args, **kwargs):
        return super(GraffitiCreateView, self).dispatch(*args, **kwargs)


class GraffitiViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Graffiti.objects.filter(active=True, checked=True)
    serializer_class = GraffitiSerializer
