import re

import scrapy

from pep_parse.constants import ALLOWED_DOMAIN, START_URL
from pep_parse.items import PepParseItem
from pep_parse.utils import make_name, make_status


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [ALLOWED_DOMAIN]
    start_urls = [START_URL]

    def parse(self, response):
        all_peps = response.css(
            '#numerical-index tbody tr a.pep.reference.internal::attr(href)'
        )
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        status = response.css('dt:contains("Status") + dd abbr::text').get()
        type_ = response.css('dt:contains("Type") + dd abbr::text').get()
        data = {
            'number': int(
                re.findall(
                    r'\d+', response.css('h1.page-title::text').get()
                )[0]
            ),
            'name': make_name(response.css('h1.page-title')),
            'status': make_status(status, type_),
        }
        yield PepParseItem(data)
