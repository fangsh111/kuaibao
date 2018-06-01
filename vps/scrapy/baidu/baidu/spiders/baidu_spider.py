import scrapy
from scrapy.http import Request
from baidu import settings, items
import datetime


class baidu_hot_spider(scrapy.Spider):
    name = 'baidu_hot'

    def __init__(self):
        self.first_url = 'http://top.baidu.com/buzz?b=1'
        self.header = settings.header_baidu

    def start_requests(self):
        return [Request(url=self.first_url, headers=self.header, callback=self.parse)]

    def parse(self, response):
        # print(response.text)
        hot_list = response.xpath('//*[@id="main"]//table[@class="list-table"]//tr')
        # print(hot_list)
        for i in range(2, len(hot_list)):
            hot_item = items.Baidu_hot_Item()
            # print(hot_list[i].extract())

            hot_item['top_num'] = hot_list[i].xpath('./td[@class="first"]/span/text()').extract_first()
            hot_item['title'] = hot_list[i].xpath('./td[@class="keyword"]/a[1]/text()').extract_first()
            # hot_item['new_link']=hot_list[i].xpath('./td[@class="tc"]/a[./text()="新闻"]/@href').extract_first()
            new_baidu_link = hot_list[i].xpath('./td[@class="tc"]/a[./text()="新闻"]/@href').extract_first()
            hot_item['video_link'] = hot_list[i].xpath('./td[@class="tc"]/a[./text()="视频"]/@href').extract_first()
            hot_item['image_link'] = hot_list[i].xpath('./td[@class="tc"]/a[./text()="图片"]/@href').extract_first()
            hot_item['hot_value'] = hot_list[i].xpath('./td[@class="last"]/span/text()').extract_first()
            if new_baidu_link:
                yield Request(url=new_baidu_link, callback=self.get_news, meta={'item': hot_item})

    def get_news(self, response):
        hot_item = response.meta['item']
        hot_item['new_link'] = response.xpath('//div[contains(./div/div[2]/p/text(),"网易")]/h3/a/@href').extract_first()
        if not hot_item['new_link']:
            hot_item['new_link'] = response.xpath(
                '//div[contains(./div/div[2]/p/text(),"新浪")]/h3/a/@href').extract_first()
        if not hot_item['new_link']:
            hot_item['new_link'] = response.xpath(
                '//div[contains(./div/div[2]/p/text(),"凤凰")]/h3/a/@href').extract_first()
        if not hot_item['new_link']:
            hot_item['new_link'] = response.url
        hot_item['create_timed'] = datetime.datetime.now()  ###记录插入时间
        hot_item['update_timed'] = datetime.datetime.now()  ####记录修改时间
        yield hot_item
