import json

from django.contrib.auth import authenticate, login
from django.core.serializers import serialize
from django.http import JsonResponse

from streamingPlatform.models.fans.fans import Fans
from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.users.users import Users

import re
def cancelFollows(request):

    user = request.user
    follow = request.GET.get('follow')

    fans = Fans.objects.filter(fan=user.username, follower=follow)

    if fans is not None:
        fans.delete()
        return JsonResponse({
            'result': 'success',
        })

    return JsonResponse({
        'result': 'failed',
    })