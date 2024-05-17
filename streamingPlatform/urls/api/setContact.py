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
from django.utils import timezone
import re
def setContact(request):

    data = request.GET
    user1 = data['user1']
    user2 = data['user2']

    user1 = Users.objects.filter(uid=user1)[0]
    user2 = Users.objects.filter(uid=user2)[0]
    print(user1, user2)
    res = userContact(user1=user1, user2=user2, end_time=timezone.now())
    res.save()

    return JsonResponse({
        'result': 'success',
    })