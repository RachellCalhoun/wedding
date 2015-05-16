from django.shortcuts import render
from .models import Entry

def index(request):
	entrys = Entry.objects.all()
	context = {'entrys':entrys}
	return render(request, 'registry/index.html',context)
