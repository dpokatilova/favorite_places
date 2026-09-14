from django import forms

class NewPlaceForm(forms.Form):
    title = forms.CharField(label='Назва місця', max_length=100)
    place_type = forms.CharField(label='Тип місця', max_length=50)
    location = forms.CharField(label='Адреса', max_length=200)
    rating = forms.IntegerField(label='Рейтинг (1-5)', min_value=1, max_value=5)
    description = forms.CharField(label='Повний опис', widget=forms.Textarea)