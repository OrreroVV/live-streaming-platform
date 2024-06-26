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

def onLiving(request):

    data = request.GET
    user = request.user

    if user is None:
        return JsonResponse({
            'result': 'failed',
        })

    users = Users.objects.filter(uid=user)[0]
    lists = liveCounts.objects.filter(uid=users.uid)
    for item in lists:
        if item.end_time is None:
            return JsonResponse({
                'result': 'failed',
            })

    res = StreamCode.objects.filter(uid=users.uid)[0]
    res.is_open = "1"
    res.save()
    new_record = liveCounts(uid=users, end_time=None)
    new_record.save()
    return JsonResponse({
        'result': 'success',
    })


