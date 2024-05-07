from django.db import models
from django.core.validators import MinValueValidator, RegexValidator

from common.utils import slugify

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Film(models.Model):
    name = models.CharField(max_length=100)
    en_name = models.CharField(max_length=100, null=True, blank=True)
    synopsis = models.CharField(max_length=1000, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0, "Duration must be greater than 1 minute")])
    poster = models.ImageField(null=True, blank=True, upload_to='film_poster/')
    genres = models.ManyToManyField(to=Genre)
    actors = models.ManyToManyField(to=Person, through='Role', related_name='acted_films')
    directors = models.ManyToManyField(to=Person, related_name='directed_films')
    trailer_link = models.URLField(null=True, blank=True)
    slug = models.CharField(default="", null=False, blank=True, max_length = 200, validators=[RegexValidator(regex=r"^[\u0E00-\u0E7Fa-zA-Z0-9_]+\Z")])

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Role(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name