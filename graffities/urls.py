from django.conf.urls import include, url
from graffities.views import IndexGraffitiList, GraffitiDetail, GraffitiCreateView
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', IndexGraffitiList.as_view(), name='index'),
    url(r'^graffiti/(?P<pk>\d+)/$', GraffitiDetail.as_view(), name='graffiti'),
    url(r'^add_graffiti$', GraffitiCreateView.as_view(), name='add_graffiti'),
    url(r'^success/', TemplateView.as_view(template_name="success.html")),
    ]
