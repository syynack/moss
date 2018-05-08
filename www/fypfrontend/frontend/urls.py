from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index),
    url(r'^retrieve', retrieve),
    url(r'^task', task),
    url(r'^execute_task', execute_task),
    url(r'^kill_task', kill_task)
]