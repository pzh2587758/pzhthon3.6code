import scrapy


class StackOverflowSpider(scrapy.Spider):  # （爬虫的基类）
    name = "stackoverflow"  # 爬虫名
    start_urls = ["http://stackoverflow.com/questions?sort=votes"]  # 链接

    def pars(self, response):  # (url储存之后的响应)
        for href in response.css('.qestion-summary h3 a::attr(href)'):  # 根据css方法抽取链接
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):
        yield{
            'title': pesponse.css('h1 a::text').extrace()[0],
            'votes': response.css(".question.vote-count-post::text").extract()[0],
            'body': response.css(".question.post-text").extract()[0],
            'tags': response.css('.question.post-tag::text').extract(),
            'link': response.url,
        }
