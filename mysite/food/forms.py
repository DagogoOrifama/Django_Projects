from django import forms
from .models import Item

# create form class to add new item 
class ItemForm(forms.ModelForm):
    # the Meta class is a class which gives more information on the ItemForm class
    class Meta:
        model = Item
        fields = ['item_name','item_desc', 'item_price', 'item_image']