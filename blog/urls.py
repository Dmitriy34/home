from django.conf.urls import url    #импортировали все методы django
from . import views                 #и все views(представления) из приложения blog

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
