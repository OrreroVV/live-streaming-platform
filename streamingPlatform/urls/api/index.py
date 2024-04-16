from django.conf.global_settings import STATIC_ROOT
from django.contrib import admin
from django.urls import path, include

from streamingPlatform.urls.api.cancelFan import cancelFan
from streamingPlatform.urls.api.cancelFollow import cancelFollows
from streamingPlatform.urls.api.getFans import getFans
from streamingPlatform.urls.api.getFollows import getFollows
from streamingPlatform.views.Register import Register
from streamingPlatform.views.Signin import Signin
from streamingPlatform.views.all_stream_code import all_stream_code
from streamingPlatform.views.liveCode import liveCode
from streamingPlatform.views.show_video_frame import show_video_frame

urlpatterns = [
    path('Signin/', Signin, name='Signin'),
    path('Register/', Register, name='Register'),
    path('liveCode/', liveCode, name='get_liveCode'),
    path('video_frame/', show_video_frame, name='video_frame'),
    path('all_stream_code/', all_stream_code, name='all_stream_code'),
    path('getfollows/', getFollows, name="getFollow"),
    path('cancelFollow/', cancelFollows, name="cancelFollows"),

    path('getfans/', getFans, name="getFollow"),
    path('cancelfan/', cancelFan, name="cancelFollows"),
]