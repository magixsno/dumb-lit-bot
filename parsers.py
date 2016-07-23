from HTMLParser import HTMLParser
from unicodedata import normalize
import json

DATA_ELEMENTS = []
INPUT_FILE = 'sci-fi-stories.txt'

# extracts the href from the discovered a tags.
class BodyExtractHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
     #   print "Encountered a start tag:", tag, attrs
        pass

    def handle_endtag(self, tag):
     #   print "Encountered an end tag :", tag
        pass

    def handle_data(self, data):
     #   print "Encountered some data  :", data
        DATA_ELEMENTS.append(data + " ")

class ParseSpiderResults():
    def parseJSON(self, json_file):
        f = open(json_file, 'r')
        decoded_json = json.loads(f.read())
        html_parser = BodyExtractHTMLParser()
        for glob in decoded_json:
            if u'body' in glob:
                for element in glob[u'body']:
                    html_parser.feed(element)
        html_parser.close()

def main():
    p = ParseSpiderResults()
    p.parseJSON('sci-fi-stories.json')

    f = open(INPUT_FILE, 'w')
    for element in DATA_ELEMENTS:
        f.write(element.encode('ASCII', 'ignore'))
    f.close()

if __name__ == '__main__':
    main()
