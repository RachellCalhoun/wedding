from django.db import models

# Create your models here.
class Entry(models.Model):
	store = models.CharField(max_length = 200)
	item = models.CharField(max_length= 200)
	price = models.PositiveIntegerField()
	location = models.CharField(max_length = 200)
	bought = models.BooleanField()
	img = models.ImageField(blank=True, null=True)