
import scrapy

class adrigo(scrapy.Spider):
    name = 'adrigospider'
    start_urls = ['https://www.adrigo.es']

    def parse(self, response):
        links = response.xpath("//div[contains(@class, 'social-links')]/a/@href").getall()
        with open("links_adrigo.txt", "w") as archivo:
            for link in links:
                archivo.write(link+"\n")
