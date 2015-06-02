
from django.shortcuts import render
from .models import Entry
from django.shortcuts import get_object_or_404, render

def rsvp(request):
	
	return render(request, 'rsvp/rsvp.html',)
