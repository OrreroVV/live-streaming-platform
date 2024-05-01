# video/consumers.py
import json
import time

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatSocket(AsyncWebsocketConsumer):
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
                'event': data['event'],
                'uid': data['uid'],
                'name': data['name'],
                'ctx': data['ctx']
            },
        )
    async def chat_message(self, data):
        print(data)

    async def group_send_event(self, data):  # 组内每一个人接收到group_send(type = group_create_player)都会执行该操作
        await self.send(text_data=json.dumps(data))

    # Receive message from WebSocket
    async def receive(self, text_data):
        data = json.loads(text_data)
        event = data['event']
        print(event, data)
        if event == 'message':
            await self.send_message(data)
        elif event == 'chat':
            await self.chat_message(data)