from django.db import models
from django.contrib.auth.models import User

class Women(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
