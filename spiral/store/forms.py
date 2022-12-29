from django import forms

from .models import Product, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'address', 'zipcode', 'city',)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('category', 'title', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'style': 'width: 100%; padding: 1rem; border-width: 1px; border-color: rgb(229 231 235);'
            }),
            'title': forms.TextInput(attrs={
                'style': 'width: 100%; padding: 1rem; border-width: 1px; border-color: rgb(229 231 235);'
            }),
            'description': forms.Textarea(attrs={
                'style': 'width: 100%; padding: 1rem; border-width: 1px; border-color: rgb(229 231 235);'
            }),
            'price': forms.TextInput(attrs={
                'style': 'width: 100%; padding: 1rem; border-width: 1px; border-color: rgb(229 231 235);'
            }),
            'image': forms.FileInput(attrs={
                'style': 'width: 100%; padding: 1rem; border-width: 1px; border-color: rgb(229 231 235);'
            })
        }