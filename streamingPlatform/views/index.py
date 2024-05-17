
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

    login_user = Users.objects.filter(uid=login_uid).get()
    main_users = Users.objects.filter(uid=uid).get()

    if login_user.user_name == main_users.user_name:
        return render(request, "living_self.html",
                      {"uid": uid, "main_user_name": main_users.user_name, "login_uid": login_uid,
                       "login_user_name": login_user_name, "live_code": user_code.code})

    if login_user.level == "0":
        return render(request, "living.html", {"uid": uid, "main_user_name" :main_users.user_name, "login_uid": login_uid, "login_user_name": login_user_name, "live_code": user_code.code})
    else:
        return render(request, "living_admin.html", {"uid": uid, "main_user_name": main_users.user_name, "login_uid": login_uid,
                                               "login_user_name": login_user_name, "live_code": user_code.code})


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

        fan = Fans.objects.filter(follower=main_uid)
        follow = Fans.objects.filter(fan=main_uid)

        fan = fan.count()
        follow = follow.count()

        if login_uid == main_uid:
            login_users = Users.objects.filter(uid=login_user.username)[0]
            if login_users.level == "1" or login_users.level == "2":
                return render(request, "user_info_admin.html",
                              {"fan": fan, "follow": follow, "login_uid": login_uid, "user_name": user_name, "url": url,
                               "uid": uid})

            return render(request, "user_info_self.html", {"fan": fan, "follow": follow, "login_uid": login_uid, "user_name": user_name, "url": url, "uid": uid})
        else:
            login_users = Users.objects.filter(uid=login_user.username)[0]
            if login_users.level == "1" or login_users.level == "2":

                return render(request, "user_info_admin.html",
                              {"fan": fan, "follow": follow, "login_uid": login_uid, "user_name": user_name, "url": url,
                               "uid": uid})

            print("get: user", login_uid, user_name, url, uid)
            return render(request, "user_info.html", {"fan": fan, "follow": follow, "login_uid": login_uid, "user_name": user_name, "url": url, "uid": uid})




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

def message(request):
    login_user = request.user
    users = Users.objects.get(uid=login_user)
    user_name = users.user_name
    print(login_user, user_name)
    return render(request ,"message.html", {"login_uid": login_user.username, "login_user_name": user_name })
