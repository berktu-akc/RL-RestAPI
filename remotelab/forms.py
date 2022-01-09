#from typing import ValuesView
from django import forms
from django.db import models
from django.db.models import fields
from .models import RemoteLab

class AC(forms.ModelForm):
    class Meta:
        model = RemoteLab
        fields = ["acInput1"]

class DC_1(forms.ModelForm):
    class Meta:
        model = RemoteLab
        fields = ["dcInput1"]

class DC_2(forms.ModelForm):
    class Meta:
        model = RemoteLab
        fields = ["dcInput2"]

class Channel1(forms.ModelForm):
    class Meta:
        model = RemoteLab
        fields = ["Channel1"]

class Channel2(forms.ModelForm):
    class Meta:
        model = RemoteLab
        fields = ["Channel2"]

class POT(forms.ModelForm):
    class Meta:
        model = RemoteLab
        fields = ["PotValue"]

class Experiment1(forms.ModelForm):
    class Meta:
        model = RemoteLab
        fields = ["acInput1","dcInput1","dcInput2","Channel1","Channel2","PotValue"]

class ImageForm(forms.ModelForm):
    class Meta:
        model = RemoteLab
        fields = ["title","content","image"]
