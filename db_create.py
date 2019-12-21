from config import SQLALCHEMY_DATABASE_URI

from app import db
from app import models
import os.path


# Creates all the tables and the database.
db.create_all()

tags = ['IT', 'English', 'Python', 'Java', 'Javascript']

for tag_name in tags:
    tag = models.Tag.query.filter(models.Tag.name == tag_name).first()
    if tag is None:
        tag = models.Tag(name=tag_name)
        db.session.add(tag)
        db.session.commit()
