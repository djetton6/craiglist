# This package will contain the spiders of your Scrapy project
# -*- coding: utf-8 -*-
# Please refer to the documentation for information on how to create and manage
# your spiders.


import scrapy


class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["newyork.craigslist.org"]
    start_urls = (
        # specific URL
        "https://newyork.craigslist.org/search/egr",
    )

    def parse(self, response):
        listings = response.xpath(
            '//a[@class="result-title hdrlnk"]/text()').extract()
        for listing in listings:
            yield {'Listing': listing}
