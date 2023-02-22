from django import forms
from . import models
class CreateForm(forms.ModelForm):
	album  = forms.CharField(max_length = 120 , required= False)
	class Meta:
		model  = models.Muscic
		fields = ('title','artist','audio_file','cover')