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
def setFollow(request):

    data = request.GET
    user1 = data['user1']
    user2 = data['user2']

    follower_user = Users.objects.filter(uid=user2)[0]
    fan_user = Users.objects.filter(uid=user1)[0]
    print(follower_user, fan_user)

    res = Fans.objects.filter(follower=follower_user, fan=fan_user)
    print(res)
    if res.exists():
        return JsonResponse({
            'result': 'success',
        })

    new_record = Fans(follower=follower_user, fan=fan_user)
    new_record.save()

    return JsonResponse({
        'result': 'success',
    })