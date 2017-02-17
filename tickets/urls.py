from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^choose$', views.tickets_choose, name='choose'),
    url(r'^$', views.tickets_list, name='tickets/tickets_list'),
]
