from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = stud
        fields = ['name', 'age']
