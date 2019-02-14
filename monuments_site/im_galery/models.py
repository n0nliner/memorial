from django.db import models


class picture(models.Model):
    slug = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/', default='none')
    class Meta:
        verbose_name_plural = "pic"


class album(models.Model):
    slug = models.DateTimeField(auto_now_add=True)
    photos = models.ManyToManyField(picture, default='none', verbose_name='pic')
    poster = models.ImageField(upload_to='uploads/', default='none')
