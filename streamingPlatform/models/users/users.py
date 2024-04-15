from django.db import models
from django.contrib.auth.models import User
class Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) # 账号密码
    uid = models.CharField(max_length=100, null=False, primary_key=True)  # 账号
    user_name = models.CharField(max_length=100, null=False)    # 用户名
    phone = models.CharField(max_length=16) # 手机号
    img_url = models.CharField(max_length=100, default='') # 头像url
    level = models.CharField(max_length=4, default='0')
