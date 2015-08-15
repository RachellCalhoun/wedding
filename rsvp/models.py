from django.db import models
from django.utils import timezone
# need to change when i know what i'm doing ...
class Entry(models.Model):
	name = models.CharField(max_length = 200)
	email = models.CharField(max_length= 200, blank=True, null=True)
	guests = models.PositiveIntegerField()
	message = models.CharField(max_length = 200, blank=True, null=True)
	diet = models.CharField(max_length = 200, blank=True, null=True)
	songrequest = models.CharField(max_length = 200, blank=True, null=True)
	coming = models.BooleanField()
	img = models.ImageField(blank=True, null=True)
	time = models.DateTimeField(default=timezone.now)