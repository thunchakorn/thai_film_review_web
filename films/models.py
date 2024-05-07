from django.db import models
from django.core.validators import MinValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

class Film(models.Model):
    name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0, "Duration must be greater than 1 minute")])
    poster = models.ImageField(null=True, blank=True, upload_to='film_poster/')
    genres = models.ManyToManyField(to=Genre)
    actors = models.ManyToManyField(to=Person, through='Role', related_name='acted_films')
    directors = models.ManyToManyField(to=Person, related_name='directed_films')
    trailer_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
