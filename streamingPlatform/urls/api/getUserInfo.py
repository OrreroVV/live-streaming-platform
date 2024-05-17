import json

from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.http import JsonResponse

from streamingPlatform.models.fans.fans import Fans
from streamingPlatform.models.liveCounts.liveCounts import liveCounts
from streamingPlatform.models.roomBans.roomBans import roomBans
from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.userBans.userBans import userBans
from streamingPlatform.models.users.users import Users
from datetime import datetime, timedelta

import re

def getUserInfo(request):

    data = request.GET
    user = request.user

    users = Users.objects.filter(uid=user)[0]
    if users.level != "1":
        return JsonResponse({
            'result': 'failed',
            'res': []
        })
    res = []
    userList = Users.objects.all()

    for item in userList:
        if item.level == "0":
            room = roomBans.objects.filter(uid=item.uid)
            room_ban = "无"
            if room.exists():
                room_ban = room[0].end_time.strftime("%Y-%m-%d %H:%M:%S")

            userItem = userBans.objects.filter(uid=item.uid)
            user_ban = "无"
            if userItem.exists():
                user_ban = userItem[0].end_time.strftime("%Y-%m-%d %H:%M:%S")
            print("ban: ", room_ban, user_ban)
            temp = {'uid': item.uid,
                    'name': item.user_name,
                    'room_ban': room_ban,
                    'user_ban': user_ban,
                    }
            print(temp)
            res.append(temp)

    json_res = json.dumps(res)
    return JsonResponse({
        'result': 'failed',
        'res': json_res
    })