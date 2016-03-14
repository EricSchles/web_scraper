import lxml.html
from app.models import *
from app import db
import json
from datetime import datetime

def parse_title(html):
    html = lxml.html.fromstring(html)
    return html.xpath('//div[@id="postingTitle"]//h1')[0].text_content().strip()
    
def parse_posting_body(html):
    html = lxml.html.fromstring(html)
    return html.xpath('//div[@class="postingBody"]')[0].text_content().strip()
    
def parse_links(html):
    html = lxml.html.fromstring(html)
    return json.dumps(html.xpath('//div[@class="postingBody"]//a/@href'))

def parse_imgs(html):
    html = lxml.html.fromstring(html)
    return json.dumps(html.xpath('//ul[@id="viewAdPhotoLayout"]//img/@src'))

def parse_posted(html):
    html = lxml.html.fromstring(html)
    date = html.xpath('//div[@class="adInfo"]')[0].text_content().strip().split("\n")[1].strip()
    return datetime.strptime(date,"%A, %B %d, %Y %I:%M %p")

def parse_location(html):
    html = lxml.html.fromstring(html)
    location = ""
    for elem in html.xpath('//div[@style="padding-left:2em;"]'):
        if "Location:" in elem.text_content():
            location = elem.text_content()
    location = location.replace("\r","").replace("\n","")
    return location.split("Location:")[1].strip()

def parse_posters_age(html):
    html = lxml.html.fromstring(html)
    return html.xpath('//p[@class="metaInfoDisplay"]')[0].text_content().split("Poster's age:")[1].strip()

    
def parse():
    for ind,row in enumerate(HTML.query.all()):
        title = parse_title(row.html)
        posting_body = parse_posting_body(row.html)
        links = parse_links(row.html)
        imgs = parse_imgs(row.html)
        posted = parse_posted(row.html)
        location = parse_location(row.html)
        posters_age = parse_posters_age(row.html)
        print type(title),type(posting_body),type(links),type(imgs),type(posted),type(location),type(posters_age)
        print 
        parsed_html = ParsedHTML(row.html,row.url,row.timestamp,posting_body,title,imgs,links,posted,posters_age,location)
        db.session.add(parsed_html)
        db.session.commit()
