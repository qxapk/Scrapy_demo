import json
import scrapy
import datetime
from scrapy import Request
from scrapy.http import HtmlResponse

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91aWQiOjc4Nzk0MSwibG9naW5fdXNlcl9rZXkiOiJhODczZjY4My1kZmJkLTQ4MDQtOWZmMS1kZmVlNjUzNGRjODcifQ.v9KXHmAokSVoT5qzMs4kTTudgJ80luM-FzjPdo71HZXfRIADvhRh8rX59tt5GUuE6HBSbHdWrMbXrHAmLzk1mQ'
}


class ProductSpider(scrapy.Spider):
    name = 'index'
    def start_requests(self):
        start = 5250000
        chunk = 1
        for i in range(start, start + chunk + 1):
            data = {"goodsId": i}
            yield Request(url='https://api.x-metash.com/api/prod/NFTMall/h5/goods/details', method="POST", headers=headers, body=json.dumps(data), meta=data)

    def parse(self, response: HtmlResponse):
        try:
            data = response.json()
            data['qx_id'] = str(response.meta['goodsId'])
            data['time'] = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))  # 爬取时间
            yield data
        except:
            data = {'goodsId': response.meta['goodsId']}
            yield Request(url='https://api.x-metash.com/api/prod/NFTMall/h5/goods/details', method="POST", headers=headers, body=json.dumps(data), meta=data)