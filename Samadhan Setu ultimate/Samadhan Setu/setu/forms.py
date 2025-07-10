from django import forms
from .models import Complaint, ContactMessage

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['name', 'email', 'phone', 'adhar', 'category', 'title', 'description', 'location', 'image_url']

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
