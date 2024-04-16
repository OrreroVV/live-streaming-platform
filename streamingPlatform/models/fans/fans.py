from django.db import models
from django.contrib.auth.models import User

from streamingPlatform.models.users.users import Users


class Fans(models.Model):
    follower = models.ForeignKey(to=Users, related_name="fans_follower", to_field='uid', on_delete=models.CASCADE)
    fan = models.ForeignKey(to=Users, related_name="fans_fan", to_field='uid', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('follower', 'fan')