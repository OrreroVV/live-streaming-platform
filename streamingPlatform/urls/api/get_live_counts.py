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

import re

class CustomEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()  # 将 datetime 对象转换为字符串
        if isinstance(o, float):
            return str(o)  # 将浮点数转换为字符串
        return super().default(o)

def get_live_counts(request):

    data = request.GET
    user = request.user
    uid = data['uid']

    counts = liveCounts.objects.filter(uid=uid)
    print(counts.count())
    res = []
    for item in counts:
        if item.end_time is not None:
            temp = {'start': item.start_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'end': item.end_time.strftime("%Y-%m-%d %H:%M:%S"),
                    'time': round((item.end_time - item.start_time).total_seconds() / 3600, 2)}
            print(temp)
            res.append(temp)

    json_res = json.dumps(res)
    return JsonResponse({
        'result': 'failed',
        'res': json_res
    })