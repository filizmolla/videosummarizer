from django import forms
from django.forms import ModelForm
from videos.models import Video

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

class VideoForm(ModelForm):
    class Meta: 
        model = Video
        fields = ['url']

        #widgets = {
        #    'url': forms.TextInput(attrs={'class': 'form-control'})
        #}