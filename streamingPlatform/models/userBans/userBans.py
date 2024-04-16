from django.db import models
from django.contrib.auth.models import User

from streamingPlatform.models.users.users import Users

class userBans(models.Model):
    uid = models.ForeignKey(to=Users, related_name="userBans_baned", to_field='uid', on_delete=models.CASCADE)
    operatorUser = models.ForeignKey(to=Users, related_name="userBans_ban", on_delete=models.CASCADE)
    end_time = models.DateTimeField()
