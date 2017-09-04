# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from craigslist.items import CraigslistItem

class JobsieSpider(scrapy.Spider):
    # Define name of spider and pages to be scraped
    name = 'jobsIE'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://dublin.craigslist.org/search/jjj']

    def parse(self, response):

        # Get all of the job record classes in the page
        jobs = response.xpath('//p[@class="result-info"]')

        # For each record in the page parse the title, url, address & date posted
        # Then go to the next page

        for record in jobs:
       
            # Create item object to capture data
            item = CraigslistItem()

            # Get title, address, dateposted and URL
            item['postTitle'] = record.xpath('a/text()').extract_first()
            item['postAddress'] = record.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
            item['postDate'] = record.xpath('time/@datetime').extract_first()[:10]
            relative_url = record.xpath('a/@href').extract_first()
            item['postUrl'] = response.urljoin(relative_url)
            yield item

            # Call the function to get the next page
            relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()

            # Get the URL for the next page
            absolute_next_url = response.urljoin(relative_next_url)

            # Recursively call the parse function to get content from the next page
            yield Request(absolute_next_url, callback=self.parse)

