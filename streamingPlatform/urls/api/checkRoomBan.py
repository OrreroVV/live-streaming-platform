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
def checkRoomBan(request):

    data = request.GET
    user = request.user
    uid = data['uid']

    items = roomBans.objects.filter(uid=uid)

    if items.exists():
        end = items[0].end_time
        current_time = timezone.now()  # 获取当前时间
        print(current_time, end)
        if current_time > end:
            print("已过期")
            items[0].delete()  # 如果过期则删除该记录
            return JsonResponse({
                'result': 'success',
                'res': "1"
            })
        else:
            return JsonResponse({
                'result': 'success',
                'res': "0"
            })

    return JsonResponse({
        'result': 'success',
        'res': "1"
    })