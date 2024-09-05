from django import forms

from . import Plat


class PlatForm(forms.ModelForm):
    class Meta:
        model = Plat
        fields = ['id', 'name', 'summary']
