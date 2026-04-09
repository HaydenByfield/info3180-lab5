# Add any model classes for Flask-SQLAlchemy here
from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserProfile(db.Model):
    _tablename_ = 'user_profiles'

    id = db.Column(db.string(80), primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    username = db.Column(db.string(80))
    password = db.Column(db.string(256))

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