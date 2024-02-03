from django import forms
from .models import Letter, RECIPIENT_CHOICES


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['recipient', 'title', 'content']


class EditLetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['recipient', 'title', 'content']

class LetterDetailsForm(forms.Form):
    additional_text = forms.CharField(widget=forms.Textarea, required=False)
    referred_to_group = forms.ChoiceField(choices=RECIPIENT_CHOICES, required=False)
    is_done = forms.BooleanField(label='Done', required=False)








