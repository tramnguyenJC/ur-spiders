from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.tickets_list, name='tickets/tickets_list'),
]