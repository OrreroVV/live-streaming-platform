import json

from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.http import JsonResponse

from streamingPlatform.models.fans.fans import Fans
from streamingPlatform.models.roomBans.roomBans import roomBans
from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.userBans.userBans import userBans
from streamingPlatform.models.users.users import Users
from datetime import datetime, timedelta
from django.utils import timezone
def is_expired(end_time):
    current_time = timezone.now()
    return end_time < current_time

import re
def setUserBan(request):

    data = request.GET
    user = request.user
    uid = data['uid']
    time = int(data['time']) # 分钟

    if user is None:
        return JsonResponse({
            'result': 'failed',
        })

    users = Users.objects.filter(uid=user.username)[0]
    if users.level == "1" or users.level == "2":
        res = userBans.objects.filter(uid=uid)
        operatorUser = Users.objects.filter(uid=user)[0]
        if res:
            res = res[0]
            if is_expired(res.end_time):
                res.end_time = timezone.now() + timezone.timedelta(minutes=time)
                res.operatorUser = operatorUser
                res.save()
            else:
                res.end_time = res.end_time + timezone.timedelta(minutes=time)
                res.operatorUser = operatorUser
                res.save()

            return JsonResponse({
                'result': 'success',
            })
        else:

            end_time = datetime.now() + timedelta(minutes=time)
            new_user = Users.objects.filter(uid=uid)[0]
            new_ban = userBans(uid=new_user, operatorUser=operatorUser, end_time=end_time)
            new_ban.save()
            return JsonResponse({
                'result': 'success',
            })


    return JsonResponse({
        'result': 'failed',
    })