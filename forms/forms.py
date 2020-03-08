from django import forms
from .models import ContactFormTemplate
from forms.models import gform
from django import forms
class ContactForm(forms.ModelForm):
      class Meta:
           model=ContactFormTemplate
           fields=['name','Address','ContactNumber','EmailAddress']
class createform(forms.ModelForm):

     class Meta:
        model= gform
        fields=['title','description']

