from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    age = forms.IntegerField(label='Your Age')
    message = forms.CharField(label='Your Message', widget=forms.Textarea)
