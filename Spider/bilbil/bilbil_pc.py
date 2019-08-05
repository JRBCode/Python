#
# bilbil_pc.py
# @author bulbasaur
# @description 
# @created 2019-07-19T21:36:19.684Z+08:00
# @last-modified 2019-07-21T20:56:12.892Z+08:00
#

import json
import requests
from lxml import etree


def get_page():
    url = 'https://www.bilibili.com/ranking?spm_id_from=333.334.b_62616e6e65725f6c696e6b.1'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    r = requests.get(url, headers=header)

    return r.text


def parse(text):
    html = etree.HTML(text)
    names = html.xpath('//div[@class="info"]/a/text()')
    links = html.xpath('//div[@class="info"]/a/@href')

    item = {}
    n = 1
    for name, links in zip(names, links):
        item['order'] = n
        item['name'] = name
        item['link'] = links
        n = n + 1
        yield item


def save2File(data):
    with open('bilbil_data.json', 'a', encoding='utf-8') as f:
        data = json.dumps(data, ensure_ascii=False) + '\n'
        f.write(data)


def run():
    data = get_page()
    items = parse(data)

    for item in items:
        save2File(item)


if __name__ == '__main__':
    run()
