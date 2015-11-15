from django.conf.urls import include, url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from .views import IndexGraffitiList, GraffitiDetail, GraffitiCreateView, GraffitiViewSet

router = DefaultRouter()
router.register(r'graffities', GraffitiViewSet)

urlpatterns = [
    url(r'^$',
        IndexGraffitiList.as_view(),
        name='index'),
    url(r'^graffiti/(?P<pk>\d+)/$',
        GraffitiDetail.as_view(),
        name='graffiti'),
    url(r'^add_graffiti$',
        GraffitiCreateView.as_view(),
        name='add_graffiti'),
    url(r'^success$',
        TemplateView.as_view(template_name="success.html"),
        name='success'),
    url(r'^api/', include(router.urls)),
]
