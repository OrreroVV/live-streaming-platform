from django.db import models
from django.contrib.auth.models import User

from streamingPlatform.models.users.users import Users


class StreamCode(models.Model):
    uid = models.ForeignKey(to=Users, to_field='uid', on_delete=models.CASCADE)
    code = models.CharField(max_length=100, null=False)
    content = models.CharField(max_length=100, default="欢迎来到我的直播间~")
    create_time = models.DateTimeField(auto_now_add=True)
    is_open = models.CharField(max_length=2, default='0')