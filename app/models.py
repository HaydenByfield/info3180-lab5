# Add any model classes for Flask-SQLAlchemy here
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class UserProfile(db.Model):
    __tablename__ = 'user_profiles'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(256))

    def __init__ (self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def is_authencticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymus(self):
        return False
    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return(self.id)
    
    def __repr__(self):
        return '<user %r>' % (self.username)
    
class MovieProfile(db.Model):
    __tablename__= 'movie_profiles'

    m_id = db.Column(db.Integer, primary_key=True)
    m_title = db.Column(db.String(80), nullable=False)
    m_desc = db.Column(db.Text, nullable=False)
    m_poster = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    
    def is_authencticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymus(self):
        return False
    
    def get_id(self):
        try:
            return unicode(self.m_id)
        except NameError:
            return(self.m_id)
    
    def __repr__(self):
        return '<movie %r>' % (self.m_title)