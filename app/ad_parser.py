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
    location = ""
    for elem in html.xpath('//div[@style="padding-left:2em;"]'):
        if "Location:" in elem.text_content():
            location = elem.text_content()
    location = location.replace("\r","").replace("\n","")
    return location.split("Location:")[1].strip()

def posters_age(html):
    html = lxml.html.fromstring(html)
    return html.xpath('//p[@class="metaInfoDisplay"]')[0].text_content().split("Poster's age:")[1].split()

