# video/consumers.py
import json
import time

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.core.cache import cache

class MessageSocket(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        user = self.scope['user']
        print(self.room_name, user, user.is_authenticated)
        self.room_group_name = 'chat_%s' % self.room_name
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )
        await self.accept()
        await self.send_initial_messages()

    async def send_initial_messages(self):
        cached_messages = cache.get(self.room_name) or []
        print(self.room_name, cached_messages)
        for data in cached_messages:
            data = json.loads(data)
            print('data: ', data)
            await self.send(text_data=json.dumps({
                'uid': data['uid'],
                'name': data['name'],
                'ctx': data['ctx'],
                'time': data['time']
            }))


    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def send_message(self, data):
        print(data)
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'group_send_event',
                'uid': data['uid'],
                'name': data['name'],
                'ctx': data['ctx'],
                'time': data['time']
            },
        )

    async def group_send_event(self, data):  # 组内每一个人接收到group_send(type = group_create_player)都会执行该操作
        await self.send(text_data=json.dumps(data))

    # Receive message from WebSocket
    async def receive(self, text_data):
        # 存储消息到缓存
        cached_messages = cache.get(self.room_name) or []
        cached_messages.append(text_data)
        cache.set(self.room_name, cached_messages)
        data = json.loads(text_data)
        await self.send_message(data)
