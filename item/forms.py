from django import forms
from .models import Item

class newItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['category','name','description','price','image']
        widgets = {
        'category':forms.Select(attrs={
            'class':'w-full p-3 rounded-xl border'
        }),
        'name': forms.TextInput(attrs={
            'class':'w-full p-3 rounded-xl border'
        }),
        'description':forms.Textarea(attrs={
            'class': 'w-full p-3 rounded-xl border'
        }),
        'price':forms.NumberInput(attrs={
            'class': 'w-full p-3 rounded-xl border'
        }),

        'image':forms.FileInput(attrs={
            'class':'w-full p-3 rounded-xl border'
        })
    }