from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name



class Movie(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    director = models.ForeignKey(Person, related_name='director_in_movie')
    actors = models.ManyToManyField(Person, through='Role', related_name='role_in_movie')
    year = models.IntegerField()

    def __str__(self):
        return self.title



class Role(models.Model):
    person = models.ForeignKey(Person)
    movie = models.ForeignKey(Movie)
    role = models.CharField(max_length=64)

    def __str__(self):
        return self.role



