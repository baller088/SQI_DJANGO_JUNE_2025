from django.db import models
from django.conf import settings
# Create your models here.

def cover_image():
    return 'default/cover.jpg'

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    instructions = models.TextField()
    cooking_time = models.IntegerField()
    image = models.ImageField(upload_to="recipe_images/", blank=True, null=True)
    cover_images = models.ImageField(upload_to="recipe_covers/", blank=True, null=True,default=cover_image)

    def __str__(self):
        return self.name