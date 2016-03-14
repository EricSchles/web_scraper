import lxml.html
from app.models import HTML
import json
from datetime import datetime

def parse_title(html):
    html = lxml.html.fromstring(html)
    return html.xpath('//div[@id="postingTitle"]/h1')[0].text_content()

def parse_posting_body(html):
    html = lxml.html.fromstring(html)
    return html.xpath('//div[@id="postingBody"]')[0].text_content()

def parse_links(html):
    html = lxml.html.fromstring(html)
    return json.dumps(html.xpath('//div[@id="postingBody"]//a/@href'))

def parse_imgs(html):
    html = lxml.html.fromstring(html)
    return json.dumps(html.xpath('//ul[@id="viewAdPhotoLayout"]//img/@src'))

def parse_posted(html):
    html = lxml.html.fromstring(html)
    date = html.xpath('//div[@class="adInfo"]')[0].text_content().split("\n")[1]
    return datetime.strptime(date,"%A, %B %d, %Y %I:%M %p")

def location(html):
    html = lxml.html.fromstring(html)
    html.xpath('//div[@class="postingBody"]')[0].text_content()
