import json

from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.http import JsonResponse

from streamingPlatform.models.fans.fans import Fans
from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.users.users import Users

import re
def getFans(request):
    user = request.user
    print("username: ", user.username)

    follows = Fans.objects.filter(follower=user.username)
    res = []

    for item in follows:
        print("fans: ", item.fan.uid)
        temp = {"uid": item.fan.uid, "img_url": item.fan.img_url, "name": item.fan.user_name}
        res.append(temp)
    # 序列化 QuerySet 为 JSON 字符串

    return JsonResponse({
        'result': 'success',
        'res': res,
    })