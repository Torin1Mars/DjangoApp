from django.db import models
from django.db.models import DateField, CharField, TextField, SlugField, DateTimeField


# Create your models here.
class Post(models.Model):
    title = CharField(max_length=60)
    body = TextField()
    slug = SlugField(max_length=100)
    date = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
