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
        return "<html %r>" % self.id

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
