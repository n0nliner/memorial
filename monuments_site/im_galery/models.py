from django.db import models


class album(models.Model):
    slug = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to='media/', default='none')
