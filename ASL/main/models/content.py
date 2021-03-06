from django.db import models
from main.models.category import Category
from main.models.country import Country
from main.models.difficulty import Difficulty
from embed_video.fields import EmbedVideoField
from django.template.defaultfilters import slugify


class Content(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200)
    vocab = models.CharField(max_length = 200, blank = True, null = True)
    difficulty = models.ForeignKey('Difficulty')
    country = models.ForeignKey('Country')
    # images = models.CharField(max_length = 200, blank = True, null = True)
    # video = models.URLField(max_length = 200)
    video = EmbedVideoField()  # same like models.URLField()
    categories = models.ManyToManyField(Category)

    def __unicode__(self):
        return str(self.pk) + self.title