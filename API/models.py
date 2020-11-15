import peewee
from database import db

class Article(peewee.Model):
    article_id = peewee.IntegerField(primary_key = True)
    name = peewee.CharField()
    price = peewee.IntegerField()
    quantity = peewee.IntegerField()

    class Meta:
        database = db

class Bill(peewee.Model):
    bill_id = peewee.IntegerField(primary_key = True)
    client_name = peewee.CharField()
    rnc = peewee.CharField()
    date = peewee.DateTimeField()
    description = peewee.CharField()
    quantity = peewee.IntegerField()
    article = peewee.ForeignKeyField(Article, backref="articles")
    sub_total = peewee.IntegerField()
    itbis = peewee.IntegerField()
    total = peewee.IntegerField()  

    class Meta:
        database = db

