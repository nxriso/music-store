from django import forms


class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    tel = forms.CharField(required=False)
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
