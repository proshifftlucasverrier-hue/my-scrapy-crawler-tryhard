import scrapy

class ExampleSpider(scrapy.Spider):
    name = 'example'
    start_urls = ['http://example.com']

    def parse(self, response):
        # Extract data from the response
        title = response.css('title::text').get()
        yield {'title': title}

        # Follow links to the next pages
        for next_page in response.css('a.next::attr(href)'):
            yield response.follow(next_page, self.parse)