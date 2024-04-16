import json

from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.http import JsonResponse

from streamingPlatform.models.fans.fans import Fans
from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.users.users import Users

import re
def getFollows(request):
    user = request.user
    print("username: ", user.username)

    fans = Fans.objects.filter(fan=user.username)
    res = []

    for item in fans:
        print("follow: ", item.follower.uid)
        temp = {"uid": item.follower.uid, "img_url": item.follower.img_url, "name": item.follower.user_name}
        res.append(temp)
    # 序列化 QuerySet 为 JSON 字符串

    return JsonResponse({
        'result': 'success',
        'res': res,
    })