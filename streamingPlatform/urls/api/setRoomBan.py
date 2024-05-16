import json

from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.http import JsonResponse

from streamingPlatform.models.fans.fans import Fans
from streamingPlatform.models.liveCounts.liveCounts import liveCounts
from streamingPlatform.models.roomBans.roomBans import roomBans
from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.users.users import Users
from datetime import datetime, timedelta
from django.utils import timezone
import re

def is_expired(end_time):
    current_time = timezone.now()
    return end_time < current_time

def setRoomBan(request):

    data = request.GET
    user = request.user
    uid = data['uid']

    time = int(data['time'])

    if user is None:
        return JsonResponse({
            'result': 'failed',
        })

    record = roomBans.objects.filter(uid=uid)
    operatorUser = Users.objects.filter(uid=user)[0]
    if record.exists():
        record = record[0]
        if is_expired(record.end_time):
            record.end_time = timezone.now() + timezone.timedelta(minutes=time)
            record.operatorUser = operatorUser
            record.save()
        else:
            record.end_time = record.end_time + timezone.timedelta(minutes=time)
            record.operatorUser = operatorUser
            record.save()

        return JsonResponse({
            'result': 'success',
        })
    else:
        end_time = datetime.now() + timedelta(minutes=time)  # 计算结束时间
        baned_user = Users.objects.get(uid=uid)
        new_record = roomBans.objects.create(uid=baned_user, end_time=end_time, operatorUser=operatorUser)
        new_record.save()

    return JsonResponse({
        'result': 'success',
    })