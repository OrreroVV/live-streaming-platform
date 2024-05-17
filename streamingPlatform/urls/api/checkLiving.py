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
def checkLiving(request):

    data = request.GET
    uid = data['uid']

    res = StreamCode.objects.filter(uid=uid)[0]
    print("res.is_open: ", res.is_open)
    return JsonResponse({
        'result': 'success',
        'res': res.is_open
    })