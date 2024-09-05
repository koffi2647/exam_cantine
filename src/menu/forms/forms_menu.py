from django import forms

from menu.models.menu_model import Menu

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['id', 'creation_date', 'plat']
