from app import db
from datetime import datetime

class Image(db.model):
    id = db.Column(db.BigInteger, primary_key=True,auto_increment=True)
    name = db.Column(db.String(250), nullable=True)
    created_at = db.Column(db.Datetime, default=datetime.utcnow)
    updated_at = db.Column(db.Datetime, default=datetime.utcnow)
    def __repr__(self):
        return '<Image {}>'.format(self)