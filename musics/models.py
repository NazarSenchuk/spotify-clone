from django.db import models
from . import helpers
from . import validators
from django.db.models import CharField,ForeignKey 
class Muscic(models.Model):
	title =  CharField(max_length= 120)
	artist =CharField(max_length= 120)
	album = ForeignKey('Album',null = True,blank = True , on_delete = models.CASCADE)
	time_length = models.DecimalField(blank = True, max_digits = 20, decimal_places =  2)
	audio_file = models.FileField(upload_to ='musics', validators =[validators.validate_is_audio])
	cover  = models.ImageField(upload_to ='music_image/',null = True)
	def save(self,*args,**kwargs):
		if not self.time_length:
			time_length  = helpers.get_audio_length(self.audio_file)
			self.time_length = time_length/60
		return super().save(*args,*kwargs)
class Album(models.Model):
	name  =  models.CharField(max_length = 100)

