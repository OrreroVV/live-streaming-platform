import cv2
import numpy as np

# FLV 流地址
flv_url = 'http://8.138.86.207/flv?port=9909&app=live&stream=dTpbsZYOEyDtgJb51khZpwlOVL0PFO4f'
rtmp_url = 'rtmp://8.138.86.207:9909/live/dTpbsZYOEyDtgJb51khZpwlOVL0PFO4f'
cap = cv2.VideoCapture(rtmp_url)
ret, frame = cap.read()

if ret:
    success, jpeg_frame = cv2.imencode('.jpg', frame)
    # 显示视频流帧


cap.release()
cv2.destroyAllWindows()
