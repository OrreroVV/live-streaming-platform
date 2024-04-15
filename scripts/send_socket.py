# send_video.py
import asyncio
import queue
import random
from threading import Thread

import websockets
import json
import base64
import time
import gc
from multiprocessing import Process, Queue
import os
import ast

q = queue.Queue()

# 向服务器端实时发送视频截图
async def send_video(websocket):

    while True:
        await asyncio.sleep(1/5)
        if q.empty():
            continue
        ID = q.get_nowait()
        print(json.dumps({
            "event": "message",
            "id": 'admin',
            'name': 'admin',
            'ctx': ID
        }))
        await websocket.send(json.dumps({
            "event": "message",
            "id": 'admin',
            'name': 'admin',
            'ctx': ID
        }))


def create():
    while True:
        time.sleep(1/10)
        q.put(random.randint(0, 360))


async def main_logic():
    async with websockets.connect('ws://127.0.0.1:8000/ws/chat/dTpbsZYOEyDtgJb51khZpwlOVL0PFO4f/', ping_interval=None) as websocket:
        await send_video(websocket)


if __name__ == '__main__':
    thread = Thread(target=create)
    thread.start()

    task = [
        main_logic()
    ]

    asyncio.get_event_loop().run_until_complete(asyncio.wait(task))
