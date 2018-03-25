from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=64)


class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    director = models.ForeignKey(Person)
    actors = models.ManyToManyField(Person, through='Role', related_name='role_in_movie')
    year = models.IntegerField()


class Role(models.Model):
    person = models.ForeignKey(Person)
    movie = models.ForeignKey(Movie)
    role = models.CharField(max_length=64)

