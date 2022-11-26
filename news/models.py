from django.db import models

# Create your models here.
class New(models.Model):
    title = models.TextField(max_length=128)
    description = models.TextField(max_length=512)
    image = models.ImageField(upload_to="images/")
    date = models.DateField(auto_created=True, auto_now=True)

