from lib import baike
from lib import sshistory_save
from lib import sshistory_get
from lib import translateBaidu
import sys
import getopt

errText = ''
try:
    if len(sys.argv) == 1:
        print('Missing query parameters.')
        exit(2)
    ssRequest = sys.argv[1]

    if len(sys.argv) > 2:
        ssType = sys.argv[2]
    else:
        ssType = 'baike'

    if ssType in ("baike", "baidu"):
        result = sshistory_get.getRequest(ssRequest, 'baike')
        if result == 'None':
            result = baike.query(ssRequest)
        else:
            print(result)
            sys.exit()
        if len(result) == 0:
            sshistory_save.saveRequest(ssRequest, result, 'baike_no_result')
            print('没有找到结果.')
        else:
            sshistory_save.saveRequest(ssRequest, result, 'baike')
            print(result)
        sys.exit()
    elif ssType in ("fy", "fanyi", "translate", "translateBaidu", "fy_zh_en", "fy_en_zh", "fy_zh_pt", "fy_pt_zh", "fy_zh_jp", "fy_jp_zh", "fy_en_jp", "fy_jp_en"):
        if ssType in ("fy", "fanyi", "translate", "translateBaidu", "fy_zh_en"):
            ssType = 'translateBaidu'
        result = sshistory_get.getRequest(ssRequest, ssType)
        if result != 'None':
            print(result)
            sys.exit()
        if ssType == 'fy_en_zh':
            result = translateBaidu.translateBaidu(ssRequest,'en','zh')
        elif ssType == 'fy_zh_pt':
            result = translateBaidu.translateBaidu(ssRequest,'zh','pt')
        elif ssType == 'fy_pt_zh':
            result = translateBaidu.translateBaidu(ssRequest,'pt','zh')
        elif ssType == 'fy_zh_jp':
            result = translateBaidu.translateBaidu(ssRequest,'zh','jp')
        elif ssType == 'fy_jp_zh':
            result = translateBaidu.translateBaidu(ssRequest,'jp','zh')
        elif ssType == 'fy_en_jp':
            result = translateBaidu.translateBaidu(ssRequest,'en','jp')
        elif ssType == 'fy_jp_en':
            result = translateBaidu.translateBaidu(ssRequest,'jp','en')
        else:
            ssType = 'translateBaidu'
            result = translateBaidu.translateBaidu(ssRequest)
        if len(result) == 0:
            sshistory_save.saveRequest(ssRequest, result, ssType)
            print('没有找到结果.')
        else:
            sshistory_save.saveRequest(ssRequest, result, ssType)
            print(result)
        sys.exit()
    elif ssType in ("-o", "--ofile"):
        pass
except:
    print(errText)
