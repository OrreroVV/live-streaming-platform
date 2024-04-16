from django.contrib import admin

from streamingPlatform.models.users.users import Users
from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.roomBans.roomBans import roomBans
from streamingPlatform.models.fans.fans import Fans
from streamingPlatform.models.userBans.userBans import userBans
# Register your models here.
admin.site.register(Users)
admin.site.register(StreamCode)
admin.site.register(userBans)
admin.site.register(Fans)
admin.site.register(roomBans)