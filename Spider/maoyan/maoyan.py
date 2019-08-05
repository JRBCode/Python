#
# maoyan.py
# @author bulbasaur
# @description 
# @created 2019-07-19T14:35:25.252Z+08:00
# @last-modified 2019-07-22T21:29:39.765Z+08:00
#

import json
import requests
from lxml import etree


def get_page(n):
    url = f'https://maoyan.com/board/4?offset={n*10}'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    r = requests.get(url, headers=header)

    return r.text


def parse(text):
    html = etree.HTML(text)
    names = html.xpath('//div[@class="movie-item-info"]/p[@class="name"]/a/@title')
    releasetime = html.xpath('//p[@class="releasetime"]/text()')

    item = {}
    for name, releasetime in zip(names, releasetime):
        item['name'] = name
        item['releasetime'] = releasetime
        yield item


def save2File(data):
    with open('maoyan_data.json', 'a', encoding='utf-8') as f:
        data = json.dumps(data, ensure_ascii=False) + '\n'
        f.write(data)


def run():
    for n in range(0, 10):
        data = get_page(n)
        items = parse(data)

        for item in items:
            save2File(item)


if __name__ == '__main__':
    run()
