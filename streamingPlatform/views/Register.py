import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from streamingPlatform.models.users.users import Users


def Register(request):
    data = request.GET
    print(data)
    username = data['username']
    password = data['password']
    rePassword = data['rePassword']
    user_id = data['user_id']

    print(username, password, rePassword, user_id)

    if password != rePassword:
        return JsonResponse({
            'result': '密码不一致',
        })

    if User.objects.filter(username=user_id).exists():
        print('用户名存在')
        return JsonResponse({
            'result': '用户名已存在',
        })

    user = User(username=user_id)
    user.set_password(password)
    user.save()

    Users.objects.create(user=user, uid=user_id, user_name=username)
    login(request, user)
    return JsonResponse({
        'result': 'success',
    })
