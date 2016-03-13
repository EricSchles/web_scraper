from app import db

class HTML(db.Model):
    __tablename__ = 'html'
    id = db.Column(db.Integer,primary_key=True)
    html = db.Column(db.String)

    def __init__(self,html):
        self.html = html
    def __repr__(self):
        return "<html %r>" % self.id
