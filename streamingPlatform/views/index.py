

from django.shortcuts import render

from streamingPlatform.models.fans.fans import Fans
from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.users.users import Users
import re

def nginx_test(request):
    return render(request, "nginx_test.html")


def signin(request):
    return render(request, "user_login.html")


def register(request):
    return render(request, "user_register.html")


def living(request):
    login_user = request.user
    login_uid = login_user.username

    uid = request.GET.get('uid')
    login_user_name = "unknown"

    if not StreamCode.objects.filter(uid=uid).exists():
        return render(request, "test.html")

    user_code = StreamCode.objects.filter(uid=uid).get()
    print(login_uid, uid, user_code.code)

    if not login_user.is_authenticated:
        login_uid = "unknown"
    else:
        login_user_name = Users.objects.filter(uid=login_uid).get().user_name

    print("living: ", uid, login_uid, user_code.code)
    return render(request, "living.html", {"uid": uid, "login_uid": login_uid, "login_user_name": login_user_name, "live_code": user_code.code})


def user_info(request):
    main_uid = request.GET.get('uid')
    login_user = request.user
    if not login_user:
        users = Users.objects.get(uid=main_uid)
        url = users.img_url
        user_name = users.user_name
        uid = main_uid
        login_uid = "unknow"
        print("get: user", login_uid, user_name, url, uid)
        return render(request, "user_info_self.html", {"login_uid": login_uid, "user_name": user_name, "url": url, "uid": uid })
    else:
        users = Users.objects.get(uid=main_uid)
        url = users.img_url
        user_name = users.user_name
        uid = users.uid
        login_uid = login_user.username
        if login_uid == main_uid:
            print("get: self", login_uid, user_name, url, uid)
            return render(request, "user_info_self.html", {"login_uid": login_uid, "user_name": user_name, "url": url, "uid": uid})
        else:
            print("get: user", login_uid, user_name, url, uid)
            return render(request, "user_info.html", {"login_uid": login_uid, "user_name": user_name, "url": url, "uid": uid})




def all_stream(request):
    login_user = request.user
    if login_user.is_authenticated:
        uid = login_user.username

        return render(request, "all_stream.html", {"login_uid": uid})
    return render(request, "user_login.html", )

def follow(request):
    login_user = request.user
    users = Users.objects.get(uid=login_user.username)

    fans = Fans.objects.filter(follower=users.uid)
    follows = Fans.objects.filter(fan=users.uid)

    fans = fans.count() if fans else 0
    follows = follows.count() if follows else 0

    return render(request, "follow.html", {"login_uid": login_user.username, "url": users.img_url, "name": users.user_name, "fans": fans, "follows": follows })

def fan(request):
    login_user = request.user
    users = Users.objects.get(uid=login_user.username)

    fans = Fans.objects.filter(follower=users.uid)
    follows = Fans.objects.filter(fan=users.uid)

    fans = fans.count() if fans else 0
    follows = follows.count() if follows else 0

    return render(request, "fan.html", {"login_uid": login_user.username, "url": users.img_url, "name": users.user_name, "fans": fans, "follows": follows })