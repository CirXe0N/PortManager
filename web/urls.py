from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dock_overview, name='dock_overview'),
    url(r'^docks/(?P<dock_id>[\w-]+)/$', views.dock_details, name='dock_details'),
    url(r'^authentication/$', views.authentication, name='authentication'),
    url(r'^logout/$', views.do_logout_request, name='logout'),
    url(r'^profile/$', views.user_profile, name='user_profile'),
]
