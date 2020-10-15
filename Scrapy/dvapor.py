import scrapy

class dvapor(scrapy.Spider):
    name = 'dvaporpider'
    start_urls = ['https://donostivapor.com/']

    def parse(self, response):
        archivo = open("links_donosti_vapor.txt", "w")
        links = response.xpath("//img/@src").getall()
        for link in links:
            archivo.write(link+"\n")
        archivo.close()
