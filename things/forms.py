"""Forms of the project."""
from django import forms
from django.core.validators import RegexValidator
# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label="Name")
    description = forms.Textarea()
    quantity = forms.NumberInput()

