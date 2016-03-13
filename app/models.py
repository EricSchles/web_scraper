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
