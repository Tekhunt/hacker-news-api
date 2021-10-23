from django.db import models

# Create your models here.

class News(models.Model):
    author = models.CharField(max_length=100)
    score = models.IntegerField(blank=True, default=0)
    title = models.CharField(max_length=150, unique=True)
    url = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
