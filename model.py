import os

from peewee import CharField
from peewee import DateTimeField
from peewee import ForeignKeyField
from peewee import Model

from playhouse.db_url import connect

db = connect(os.environ.get('DATABASE_URL', 'sqlite:///my_database.db'))


class User(Model):

    name = CharField(max_length=255, primary_key=True, unique=True)
    password = CharField(max_length=255)

    class Meta:
        database = db


class Task(Model):

    name = CharField(max_length=255)
    performed = DateTimeField(null=True)
    performed_by = ForeignKeyField(model=User, null=True)

    class Meta:
        database = db
