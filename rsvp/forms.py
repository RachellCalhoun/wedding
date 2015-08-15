from django import forms
from .models import Entry

class RsvpForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ("Name", "Email or PHone","Message","RSVP","Diet")