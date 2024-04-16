import json

from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.http import JsonResponse

from streamingPlatform.models.fans.fans import Fans
from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.users.users import Users

import re
def cancelFan(request):

    user = request.user
    fan = request.GET.get('fan')

    follow = Fans.objects.filter(fan=fan, follower=user.username)
    print("follow: ", follow)
    if follow is not None:
        follow.delete()
        return JsonResponse({
            'result': 'success',
        })

    return JsonResponse({
        'result': 'failed',
    })