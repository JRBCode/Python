#
# mao_downlaod.py
# @author bulbasaur
# @description 
# @created 2019-07-19T17:49:53.645Z+08:00
# @last-modified 2019-07-24T00:06:12.465Z+08:00
#

import urllib.request

def download(width, height):
    req = urllib.request.Request('http://placekitten.com/g/%s' % (width) + '/%s' % (height))
    response = urllib.request.urlopen(req)
    cat_img = response.read()

    with open('cat_%s' % (width) + '_%s' % (height) + '.jpg', 'wb') as f:
        f.write(cat_img)


def run():
    width = input("请输入照片的宽度：")
    height = input("请输入照片的长度：")
    download(width, height)


run()