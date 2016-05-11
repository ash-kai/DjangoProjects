from django.conf.urls import url

from . import views

app_name = 'ToDo'
urlpatterns = [
    url(r'^$', views.HelloUser, name='index'),
    url(r'your-name/', views.Hey, name='Greet'),
    url(r'error', views.error, name="Error"),
    url(r'[0-9a-zA-Z]+', views.default, name='Default'),
]
