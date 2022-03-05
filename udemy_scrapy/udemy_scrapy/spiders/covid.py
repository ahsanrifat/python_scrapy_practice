import scrapy


class CovidSpider(scrapy.Spider):
    name = 'covid_new_case'
    allowed_domains = ['www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        new_case_block=response.css("li.news_li")
        for new_case in new_case_block:
            ans={
                "country":new_case.css("a::text").extract_first(),
                "number_of_new_case":int(str(new_case.css("strong::text").extract_first()).split(" ")[0].replace(",",""))
            }
            print("Data->",ans)
            yield ans
