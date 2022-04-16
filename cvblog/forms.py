from django import forms
from django.contrib.auth import get_user_model

from . import models

User = get_user_model()


class CvForm(forms.ModelForm):
    edit_cv = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Cv
        fields = ['nomcv', 'sexe', 'matrimoniale', 'enfant', 'telephone', 'formation', 'competence', 'experience_A', 'experience_P', 'langue', 'certifications', 'reference', 'description']


class DeleteCvForm(forms.Form):
    delete_cv = forms.BooleanField(widget=forms.HiddenInput, initial=True)


class LettreForm(forms.ModelForm):
    edit_lettre = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Lettre
        fields = ['date', 'ville','profession', 'destinateur', 'objet', 'lettre', 'jointe']


class DeleteLettreForm(forms.Form):
    delete_lettre = forms.BooleanField(widget=forms.HiddenInput, initial=True)

class ContactForm(forms.ModelForm):
    edit_contact = forms.BooleanField(widget=forms.HiddenInput, initial=True)

    class Meta:
        model = models.Contact
        fields = ['message']


class DeleteContactForm(forms.Form):
    delete_contact = forms.BooleanField(widget=forms.HiddenInput, initial=True)
