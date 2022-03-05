import scrapy


class CovidSpider(scrapy.Spider):
    name = 'population'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/population/']

    def parse(self, response):
        country_block=response.xpath("//h2[normalize-space(text())='Population of Countries']/following::ul")[0].css("a")
        try:
            for country in country_block:
                ans={
                    # "country":country.css('a::text').extract(),
                    "country":country.xpath('.//text()').get(),
                    # "link":self.allowed_domains[0]+str(country.css('a::attr(href)').extract()[0])
                    "link":self.allowed_domains[0]+str(country.xpath(".//@href").get())
                }
                print("Data->",ans)
                yield ans
                # yield scrapy.Request(url=ans['link'])
        except Exception as e:
            print("Exception-->",e)
