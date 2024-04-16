import json

from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from streamingPlatform.models.streamCode.streamCode import StreamCode
from streamingPlatform.models.users.users import Users

import re

def spider():
    import requests
    import xml.etree.ElementTree as ET
    url = 'http://8.138.86.207/stat'

    response = requests.get(url)

    data = response.text
    root = ET.fromstring(data)
    # 处理包含正在推流的流信息的响应数据
    nums = 0
    specific_element = root.find('.//live/nclients')  # 查找名为 element2 的元素
    if specific_element is not None:
        content = specific_element.text
        nums = content

    streams = []
    result = re.findall('<name>(.*?)</name>', data)
    for key in result:
        if key != "live":
            streams.append(key)

    return streams


def all_stream_code(request):

    streams = spider()

    res = []
    for i in streams:
        obj = StreamCode.objects.filter(code=i).get()
        uid = obj.uid.uid
        name = obj.uid.user_name
        res.append((i, uid, name))

    print("streams: ", res)
    json_res = json.dumps(res)

    return JsonResponse({
        'result': 'success',
        'json_streams': json_res
    })