from django.conf.urls import url

from . import views

app_name = 'ToDo'
urlpatterns = [
    url(r'index', views.index, name='index'),
    url(r'login', views.user_login, name="Login"),
    url(r'profile', views.profile_create, name='Profile'),
    url(r'^(?P<id>\d+)/prfileEdit/$', views.profile_update, name='Profile Update'),    
    url(r'^notification$', views.notification, name='Notification'),
    url(r'^(?P<id>\d+)/notificationEdit$', views.notification_update, name='NotificationUpdate'),
    url(r'notificationCreate', views.notification_create, name='Notification Create'),
    url(r'^(?P<id>\d+)/notificationDelete$', views.notification_delete, name='Notification Delete'),
    url(r'task', views.task, name='Task'),
    url(r'taskCreate', views.task_create, name='Task'),
    url(r'error', views.error, name='Error'),
    url(r'success', views.success, name='Success'),
    #url(r'[0-9a-zA-Z]+', views.default, name='Default'),
]
