from django.conf.global_settings import STATIC_ROOT
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from streamingPlatform.views.index import signin, living, register, all_stream, follow, fan, message
from streamingPlatform.views.index import user_info

urlpatterns = [
    # path("", index, name="index"),
    # path("foods/", foods, name="foods"),
    path("api/", include("streamingPlatform.urls.api.index")),
    path('signin/', signin, name='signin'),
    path('register/', register, name='register'),
    path('user_info/', user_info, name="user_info"),
    path('living/', living, name="living"),
    path('all_stream/', all_stream, name="all_stream"),
    path('follow/', follow, name="follow"),
    path('fan/', fan, name="fan"),
    path('message/', message, name="message"),
]
