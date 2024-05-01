import json

from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.http import JsonResponse

from streamingPlatform.models.fans.fans import Fans
from streamingPlatform.models.roomBans.roomBans import roomBans
from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.users.users import Users
from datetime import datetime, timedelta

def is_expired(end_time):
    current_time = datetime.now()
    return end_time < current_time

import re
def banRoom(request):

    data = request.GET
    user = request.user
    uid = data['user_id']
    time = data['ban_time'] # 分钟

    if user is None:
        return JsonResponse({
            'result': 'failed',
        })

    users = Users.objects.filter(uid=user.username)[0]
    if users.level == 1 or users.level == 2:
        res = roomBans.objects.filter(uid=uid)
        if res.exists():
            res = res[0]
            if is_expired(res.end_time):
                res.end_time = datetime.now() + timedelta(minutes=time)
                res.save()
            else:
                res.end_time = res.end_time + timedelta(minutes=time)
                res.save()

            return JsonResponse({
                'result': 'success',
            })
        else:
            end_time = datetime.now() + timedelta(minutes=time)
            new_ban = roomBans(uid=uid, operatorUser=user.username, end_time=end_time)
            new_ban.save()
            return JsonResponse({
                'result': 'success',
            })


    return JsonResponse({
        'result': 'failed',
    })