import lxml.html
from app.models import HTML
import json

def parse_title(html):
    html = lxml.html.fromstring(html)
    return html.xpath('//div[@id="postingTitle"]/h1').text_content()

def parse_posting_body(html):
    html = lxml.html.fromstring(html)
    return html.xpath('//div[@id="postingBody"]').text_content()

def parse_links(html):
    html = lxml.html.fromstring(html)
    html.xpath('//div[@id="postingBody"]//a/@href')
