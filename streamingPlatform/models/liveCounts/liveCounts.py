from django.db import models
from django.contrib.auth.models import User

from streamingPlatform.models.users.users import Users


class liveCounts(models.Model):
    uid = models.ForeignKey(to=Users, to_field='uid', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)