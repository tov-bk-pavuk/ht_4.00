from django import forms


class Triangle(forms.Form):
    side_1 = forms.IntegerField(label='Сторона 1', min_value=1)
    side_2 = forms.IntegerField(label='Сторона 2', min_value=1)
