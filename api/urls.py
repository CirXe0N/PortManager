from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^ships/(?P<ship_slug>[a-zA-Z0-9-]+)/$', views.ShipsView.as_view()),
]