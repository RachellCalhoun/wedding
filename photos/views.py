

from django.shortcuts import get_object_or_404, render

def photos(request):
	return render(request, 'photos/photos.html', {})
# I need to set up api via instagram but they us JS so try a workaround?def getphotos():

