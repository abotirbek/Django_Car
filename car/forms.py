from django import forms
from .models import Car

class CarForm(forms.Form):
    brand=forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class': 'form-control'}))
    model = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    year = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    color = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    mileage = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))

    def save(self,):
        brand = self.cleaned_data.get('brand')
        model = self.cleaned_data.get('model')
        year = self.cleaned_data.get('year')
        color = self.cleaned_data.get('color')
        price = self.cleaned_data.get('price')
        mileage = self.cleaned_data.get('mileage')
        return Car.objects.create(
            brand=brand,
            model=model,
            year=year,
            color=color,
            price=price,
            mileage=mileage
        )

    def clean_brand(self):
        data = self.cleaned_data.get('brand')
        if 'toyota' == data.lower():
            raise forms.ValidationError(f"{data.upper()} is denied!")
        return data

    def clean_model(self):
        data = self.cleaned_data.get('model')
        if 'byd' == data.lower():
            raise forms.ValidationError(f"{data.upper()} is denied!")
        return data

    def clean(self):
        data = super().clean()
        model = self.cleaned_data.get('model')
        brand = self.cleaned_data.get('brand')
        if model and brand:
            if brand.lower() in model.lower():
                raise forms.ValidationError("Brand title should NOT be in model title")
        return data