import json

from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.http import JsonResponse

from streamingPlatform.models.fans.fans import Fans
from streamingPlatform.models.liveCounts.liveCounts import liveCounts
from streamingPlatform.models.roomBans.roomBans import roomBans
from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.userContact.userContact import userContact
from streamingPlatform.models.users.users import Users
from datetime import datetime, timedelta

import re


def getContact(request):

    data = request.GET
    user = request.user
    uid = data['uid']

    list1 = userContact.objects.filter(user1=uid)
    list2 = userContact.objects.filter(user2=uid)
    res = []
    for item in list1:
        res.append({"uid": item.user2.uid, "name": item.user2.user_name})
    for item in list2:
        res.append({"uid": item.user1.uid, "name": item.user1.user_name})

    res = json.dumps(res)
    return JsonResponse({
        'result': 'success',
        'res': res
    })