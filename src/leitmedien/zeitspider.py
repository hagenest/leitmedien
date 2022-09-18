import imp
import scrapy
from article import Article

class ZeitspiderSpider(scrapy.Spider):
    name = 'zeitspider'
    allowed_domains = ['zeit.de']
    start_urls = ['http://zeit.de/']

    def parse(self, response):
        Article = Article=