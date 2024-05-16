from django.db import models
from django.contrib.auth.models import User

from streamingPlatform.models.users.users import Users

class userContact(models.Model):
    user1 = models.ForeignKey(to=Users, related_name="user1", to_field='uid', on_delete=models.CASCADE)
    user2 = models.ForeignKey(to=Users, related_name="user2", on_delete=models.CASCADE)
    end_time = models.DateTimeField()
