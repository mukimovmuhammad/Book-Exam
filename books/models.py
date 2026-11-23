from django.db.models import *
from accounts.models import Profile

class Book(Model):
    BOOK_STATUS = [
        ('New','Новый'),
        ('Good','Хорошо'),
        ('Normal','Нормально'),
        ('Bad','Плохо')
    ]

    title = CharField(max_length=200)
    author = CharField(max_length=120)
    owner = ForeignKey(Profile, on_delete=CASCADE)
    book_status = CharField(choices=BOOK_STATUS)
    book_added_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Exchange(Model):
    STATUS = [
        ('PENDING','В Ожидании'),
        ('BUSY','Занят'),
    ]
    book = ForeignKey(Book, on_delete=CASCADE)
    getter = ForeignKey(Profile, on_delete=CASCADE)
    trade_at = DateTimeField(auto_now_add=True)

class City(Model):
    name = CharField(max_length=140)
    def __str__(self):
        return self.name

class Genre(Model):
    name = CharField(max_length=140)
    def __str__(self):
        return self.name
