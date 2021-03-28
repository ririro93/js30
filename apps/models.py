from django.db import models

# Create your models here.
class App(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    overview = models.TextField()
    image = models.ImageField(upload_to='apps', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)