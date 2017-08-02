##

from journal.items import JournalItem
from scrapy import Spider, Request

class JournalSpider(Spider):
    name = 'journal_spider'
    allowed_urls = ['http://datascience.codata.org']
    start_urls = ['http://datascience.codata.org/articles']

    def parse(self, response):
        links =response.xpath('//div[@class="pagination pagination-centered"]/ul/li/a/@href').extract()
        for link in links:
            url='http://datascience.codata.org' + link
            yield Request(url, callback=self.parse_link)

    def parse_link(self,response):
        paper_links=response.xpath('//div[@class="article-caption"]/div/a/@href').extract()
        type = response.xpath('//span[@class="main-color-text"]/strong/text()').extract_first()
        date = response.xpath('.//p[@class="article-date"]/text()').extract_first().strip()
        for paper_link in paper_links:
            new_url = 'http://datascience.codata.org' + paper_link#
            yield Request(new_url, callback=self.parse_article,
                              meta={'date':date, 'type':type})

    
    def parse_article(self, response):
        date = response.meta['date']
        type = response.meta['type']
        title = response.xpath('//div[@class="article-title"]/h1/text()').extract_first()  #Title
        author = response.xpath('//span[@class="author-hover"]/text()').extract() #Name
        email = response.xpath('.//div[@class="author-block"]/h4/a/@href').extract_first() #Email
        keyword = response.xpath('//span[@class="span-citation"]/a/text()').extract()[:-1] #Keyword
        keyword2 = response.xpath('//div[@class="authors"]/h5/a/text()').extract()


        item = JournalItem()
        item['type'] = type
        item['title'] = title
        item['author'] = author
        item['email'] = email
        item['keyword'] = keyword
        item['keyword2'] = keyword2
        item['date'] = date


        yield item


