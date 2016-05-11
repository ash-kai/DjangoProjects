from django.conf.urls import url

from . import views

app_name = 'ToDo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'createUser', views.account, name='Account'),
    url(r'notification', views.notification, name='Notification'),
    url(r'task', views.task, name='Task'),
    url(r'error', views.error, name='Error'),
    url(r'success', views.success, name='Success'),
    url(r'[0-9a-zA-Z]+', views.default, name='Default'),
]
