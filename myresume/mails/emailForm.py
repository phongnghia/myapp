from django.forms import ModelForm
from django import forms
from myresume.mails.email import EmailMyresume


class EmailMyresumeForm(ModelForm):
    class Meta:
        fields = ['your_name', 'your_email', 'email_subject', 'email_description']
        model = EmailMyresume


class EditForm(forms.Form):
    rendered_template = "form_email.html"
