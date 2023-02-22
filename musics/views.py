from django.shortcuts import  render,redirect
from . import models
from . import forms
def home(request):
	music = models.Muscic.objects.all()
	music_list = list(models.Muscic.objects.all().values())
	return render( request,'home.html',{'music':music , 'music_list' : music_list})
def create(request):
	form = forms.CreateForm()
	if request.method == 'POST':
		form = forms.CreateForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			album = form.cleaned_data.get('album')
			if album :
				music_album,created = models.Album.objects.get_or_create(name = album)
				instance.album = music_album
				instance.save()
			else :
				instance.save() 
		return redirect('musics:home_page')
	data = {
	'form': form
	}
	return render(request , 'addPage.html',data)