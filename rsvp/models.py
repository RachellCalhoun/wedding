from django.db import models

# need to change when i know what i'm doing ...
class Entry(models.Model):
	store = models.CharField(max_length = 200)
	item = models.CharField(max_length= 200)
	price = models.PositiveIntegerField()
	location = models.CharField(max_length = 200)
	bought = models.BooleanField()
	img = models.ImageField()