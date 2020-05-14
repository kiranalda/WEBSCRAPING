import scrapy

from ..items import TechCrunchItem

class TechCrunch(scrapy.Spider):
    name='techcrunch'
    allowed_domains = ['techcrunch.com/feed']
    start_urls = ['http://techcrunch.com/feed/']

    def parse(self, response):
        titles = response.xpath('//item/title/text()').extract()
        # authors = response.xpath('//item/creator/text()').extract()
        dates = response.xpath('//item/pubDate/text()').extract()
        links = response.xpath('//item/link/text()').extract()


        for i in range(len(titles)):
            item = TechCrunchItem()
            item['title'] = titles[i]
            # print("\n\n-->", authors)
            item['pubDate'] = dates[i]
            item['link'] = links[i]

            print(item)
            yield item