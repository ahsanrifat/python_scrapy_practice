# -*- coding: utf-8 -*-
import scrapy


class JokesSpider(scrapy.Spider):
    name = 'jokes'
    allowed_domains = ['http://www.laughfactory.com/jokes/family-jokes']
    start_urls = ['http://www.laughfactory.com/jokes/family-jokes']

    def parse(self, response):
        # jokes_list=response.xpath("//div[@class='jokes']/div[@class='joke-msg']/div[@class='joke-text']/p[descendant-or-self::text()]").extract()
        jokes_list=response.xpath("//div[@class='jokes']")
        count=0
        for joke in jokes_list:
            count+=1
            result={
                'count':count,
                'joke_text':joke.xpath(".//div[@class='joke-msg']/div[@class='joke-text']/p/text()").extract()
                # 'joke_text':joke.css("div.joke-msg div.joke-text p::text")
                # 'joke_text':str(joke).strip().replace(r"\r","").replace(r"\n","")
            }
            print("Result--->",result)
            yield result