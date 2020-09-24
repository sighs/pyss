import re
import urllib.parse
import urllib.request
import hashlib
import urllib
import random
import json
import time
import sys
from translate import Translator

appid = '20200923000571767'
secretKey = 'LVzJN4b_2KAv0OXUjbDz'
url_baidu = 'http://api.fanyi.baidu.com/api/trans/vip/translate'


def translateBaidu(text, f='zh', t='en'):
    
    salt = random.randint(32768, 65536)
    sign = appid + text + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = url_baidu + '?appid=' + appid + '&q=' + urllib.parse.quote(text) + '&from=' + f + '&to=' + t + \
        '&salt=' + str(salt) + '&sign=' + sign
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    data = json.loads(content)
    result = str(data['trans_result'][0]['dst'])
    return result

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print('缺少必要参数.')
        exit(2)
    result = translateBaidu(sys.argv[1])
    print(result)
