from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """Формы подписки по емейл"""

    class Meta:
        model = Contact
        fields = ('email',)
        widgets = {
            'email': forms.TextInput(attrs={'class': 'editcontent', 'placeholder': 'Your email...'})
        }
        labels = {
            'email': ''
        }
