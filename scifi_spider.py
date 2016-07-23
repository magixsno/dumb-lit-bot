import scrapy
from HTMLParser import HTMLParser

DOMAIN = 'http://dailysciencefiction.com'
URLS = []

# extracts the href from the discovered a tags.
class ATagHrefHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        #print "Processing a start tag:", tag, attrs
        if tag == 'a':
            for attr_tag in attrs:
                if attr_tag[0] == u'href':
         #           print "FOUND URL:: " + attr_tag[1]
                    URLS.append(attr_tag[1])


    def handle_endtag(self, tag):
        #print "Encountered an end tag :", tag
        pass

    def handle_data(self, data):
        #print "Encountered some data  :", data
        pass
        
# crawler to extract the story from all the discovered links on the theme page.
class SciFiLitSpider(scrapy.Spider):
    name = 'daily_science_fiction'
    start_urls = [
    'http://dailysciencefiction.com/science-fiction/aliens',
    'http://dailysciencefiction.com/science-fiction/biotech',
    'http://dailysciencefiction.com/science-fiction/clones',
    'http://dailysciencefiction.com/science-fiction/disaster-apocalypse',
    'http://dailysciencefiction.com/science-fiction/future-societies', 
    'http://dailysciencefiction.com/science-fiction/nanotech',
    'http://dailysciencefiction.com/science-fiction/other-worlds-sf',
    'http://dailysciencefiction.com/science-fiction/robots-and-computers',
    'http://dailysciencefiction.com/science-fiction/space-travel',
    'http://dailysciencefiction.com/science-fiction/superhero',
    'http://dailysciencefiction.com/science-fiction/time-travel',
    'http://dailysciencefiction.com/science-fiction/virtual-reality',
    'http://dailysciencefiction.com/science-fiction/science-fiction'
    ]
    
    def parse(self, response):
        for href in response.css('.storyListTitle'):
            full_url = response.urljoin(href.extract())
            parser = ATagHrefHTMLParser()
            parser.feed(href.extract())
            parser.close()
            for url in URLS:
                yield scrapy.Request(DOMAIN + url, callback=self.parse_question)

    def parse_question(self, response):
        yield {
            'body': response.css('.storyText').extract(),
            'link': response.url,
        }