import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from streamingPlatform.models.users.users import Users

def Signin(request):
    data = request.GET
    print(data)
    username = data['username']
    password = data['password']
    user = authenticate(username=username, password=password)

    if not user:
        return JsonResponse({
            'result': "用户名或密码错误",
        })

    users = Users.objects.filter(user=user)

    if not users.exists():
        return JsonResponse({
            'result': "用户名或密码错误",
        })

    level = users[0].level
    print(level)

    login(request, user)
    return JsonResponse({
        'result': 'success',
    })