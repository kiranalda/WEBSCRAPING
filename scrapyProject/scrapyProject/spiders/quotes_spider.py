import scrapy
from scrapy.loader import ItemLoader
from ..items import QuotesItem
from ..pipelines import MySQLPipeLine


class QuotesSpider(scrapy.Spider):
    name = "quotes"
	
	
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
			
			
    def parse(self, response):
        self.logger.info("This is an item page %s" , response.url)
        for quote in response.css("div.quote"):
            item = QuotesItem()
            item['text'] = quote.css("span.text::text").get()
            item['author'] = quote.css("small.author::text").get()
            item['tags'] = quote.css("div.tags a.tag::text").getall()
            #item['last_upd_time'] = '2020-05-12 19:54:00'
            print(item)
            yield item
