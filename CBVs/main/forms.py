from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    age = forms.IntegerField()
    message = forms.CharField(max_length=200)
