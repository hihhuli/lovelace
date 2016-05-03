from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^statistics/(?P<content_slug>[^/]+)/$', views.content_feedback_stats, name='statistics'),
    url(r'^(?P<content_slug>[^/]+)/(?P<feedback_slug>[^/]+)/receive-content/$', views.receive_content_feedback, name='receive_content_feedback'),
    url(r'^(?P<instance_slug>[^/]+)/(?P<feedback_slug>[^/]+)/receive-emb/$', views.receive_emb_feedback, name='receive_emb_feedback'),
]
