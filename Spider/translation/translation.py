#
# translation.py
# @author JRB
# @description 
# @created 2019-07-19T18:15:12.148Z+08:00
# @last-modified 2019-07-22T17:23:01.093Z+08:00
#

import urllib.request
import urllib.parse
import json

def run():
    connect = input('请输入需要翻译的内容：')

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
    data = {}
    data['i'] = connect
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '15635314886553'
    data['sign'] = '356306c74f4cbe3ad51445d585aa0b9d'
    data['ts'] = '1563531488655'
    data['bv'] = 'bbb3ed55971873051bc2ff740579bb49'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_REALTlME'

    data = urllib.parse.urlencode(data).encode('utf-8')
    response = urllib.request.urlopen(url, data)
    html = response.read().decode('utf-8')

    target = json.loads(html)
    # print(target)
    print('翻译结果：%s' % (target['translateResult'][0][0]['tgt']) + '\n\n')


def test():
    run()
    mark = input('输入"y"继续翻译，输入其他退出')
    while mark == 'y':
        run()
        mark = input('输入"y"继续翻译，输入其他退出')


test()