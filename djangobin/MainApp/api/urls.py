from django.conf.urls import url
from MainApp.api.views import (MsgListAPIView,
                              MsgDetailView,
                              MsgUpdateView,
                              MsgDeleteView,
                              MsgCreateAPIView,
                              )

urlpatterns = [
    url(r'^$', MsgListAPIView.as_view(), name='api-list'),
    url(r'^create/$',MsgCreateAPIView.as_view(),name='api-crete'),
    url(r'^(?P<pk>\d+)/$', MsgDetailView.as_view(), name='api-detail'),
    url(r'^(?P<pk>\d+)/update/$', MsgUpdateView.as_view(), name='api-update'),
    url(r'^(?P<pk>\d+)/delete/$', MsgDeleteView.as_view(), name='api-delete')
]
