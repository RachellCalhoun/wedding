from django.shortcuts import render
from .models import Entry
from django.shortcuts import get_object_or_404, render

def index(request):
	entries = Entry.objects.all()
	context = {'entries':entries}
	return render(request, 'registry/index.html',context)

