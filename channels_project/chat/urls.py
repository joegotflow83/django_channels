from django.conf.urls import url

from chat import views


urlpatterns = [
    url(r'^$', views.about, name='about'),
    url(r'new/$', views.new_room, name='new_room'),
    url(r'^(?P<label>).*/$', views.chat_room, name='chat_room'),
]
