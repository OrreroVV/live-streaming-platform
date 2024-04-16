import numpy as np
from django.http import HttpResponse, JsonResponse
import requests
from PIL import Image
from io import BytesIO

from django.shortcuts import render
import os
import time
import shutil

def show_video_frame(request):
    stream_code = request.GET.get('stream_code')
    import subprocess
    import cv2

    image_path = 'streamingPlatform/static/video_frame/' + stream_code + '.jpeg'
    url = stream_code + ".jpeg"

    if os.path.exists(image_path):
        created_time = os.path.getctime(image_path)
        current_time = time.time()  # 获取当前时间戳
        # 计算文件创建时间距离当前时间的差值（单位为秒）
        time_difference = current_time - created_time
        if time_difference < 86400:  # 86400 秒等于一天
            return JsonResponse({
                'result': 'success',
                'video_frame_url': url
            })

    # FLV 流地址
    # flv_url = 'http://8.138.86.207/flv?port=9909&app=live&stream=' + stream_code
    rtmp_url = 'rtmp://8.138.86.207:9909/live/' + stream_code
    cap = cv2.VideoCapture(rtmp_url)
    ret, frame = cap.read()
    jpeg_frame = ""
    if ret:
        success, encoded_frame = cv2.imencode('.jpg', frame)

        # 将编码后的帧数据保存为图片
        if success:

            with open(image_path, 'wb') as file_stream:
                file_stream.write(encoded_frame.tobytes())

            print('url: ', url)
            return JsonResponse({
                'result': 'success',
                'video_frame_url': url
            })
    else:
        return JsonResponse({
            'result': 'failed',
        })