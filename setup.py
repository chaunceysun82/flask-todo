"""
Scripts to run to set up our database
"""
from passlib.hash import pbkdf2_sha256
from datetime import datetime

from model import Task
from model import User
from model import db

db.connect()
db.drop_tables([User, Task])
db.create_tables([User, Task])

User.create(name="admin", password=pbkdf2_sha256.hash("password"))
User.create(name="bob", password=pbkdf2_sha256.hash("bobbob"))

Task.create(name="Do the laundry")
Task.create(name="Do the dishes", performed=datetime.now())