import json
import secrets
import string
from random import random

from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.users.users import Users


def liveCode(request):
    data = request.GET
    user = request.user

    if not user:
        return JsonResponse({
            'result': '账号未登录',
        })

    res = ""

    user_code = StreamCode.objects.filter(uid=user.username).first()
    if not user_code:
        alphabet = string.ascii_letters + string.digits
        res = ''.join(secrets.choice(alphabet) for _ in range(32))

        user_instance = Users.objects.get(user=request.user)
        it = StreamCode(uid=user_instance, code=res)
        it.save()
    else:
        res = user_code.code

    return JsonResponse({
        'result': 'success',
        'code': res
    })
