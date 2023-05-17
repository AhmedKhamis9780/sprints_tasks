# import form class from django
from django import forms
from django.forms import ModelForm
from .models import *

# import StudentModel from models.py
# create a ModelForm
class StudentForm(forms.ModelForm):
# specify the name of model to use
    class Meta:
        model = info
        fields = "__all__"

class PostForm(ModelForm):
    class Meta:
        # write the name of models for which the form is made
        model = Post
        # Custom fields
        fields =["username", "gender", "text"]
        # this function will be used for the vali
    def clean(self):
        # data from the form is fetched using
        super(PostForm, self).clean()
        # extract the username and text field from the data
        username = self.cleaned_data.get('username')
        text = self.cleaned_data.get('text')
        # conditions to be met for the username length
        if len(username) < 5:
            self._errors['username'] = self.error_class(['Minimum 5 characters required'])
        if len(text) <10:
            self._errors['text'] = self.error_class(['Post Should Contain a minimum of 10 characters'])
        # return any errors if found
        return self.cleaned_data