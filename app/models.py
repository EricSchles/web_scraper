from app import db
from datetime import datetime

class HTML(db.Model):
    __tablename__ = 'html'
    id = db.Column(db.Integer,primary_key=True)
    html = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    url = db.Column(db.String)
    
    def __init__(self,html,url):
        self.html = html
        self.url = url
        self.timestamp = datetime.now()
        
    def __repr__(self):
        return "<html %r>" % self.url

class ParsedHTML(db.Model):
    __tablename__ = 'parsed_html'
    id = db.Column(db.Integer,primary_key=True)
    html = db.Column(db.String)
    timestamp = db.Column(db.DateTime)
    url = db.Column(db.String)
    posting_body = db.Column(db.String)
    title = db.Column(db.String)
    img_urls = db.Column(db.String)
    links = db.Column(db.String)
    date_posted = db.Column(db.String)
    posters_age = db.Column(db.String)
    location = db.Column(db.String)

    def __init__(self,html,url,timestamp,posting_body,title,img_urls,links,date_posted,posters_age,location):
        self.html = html
        self.url = url
        self.timestamp = timestamp
        self.posting_body = posting_body
        self.title = title
        self.img_urls = img_urls
        self.links = links
        self.date_posted = date_posted
        self.posters_age = posters_age
        self.location = location
        
    def __repr__(self):
        return "<html %r>" % self.url
