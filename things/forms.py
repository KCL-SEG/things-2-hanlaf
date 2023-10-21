"""Forms of the project."""
from django import forms
from django.core.validators import MinValueValidator
# Create your forms here.

class ThingForm(forms.Form):
    name = forms.CharField(label="Name")
    description = forms.CharField(widget=forms.Textarea)
    quantity = forms.Field(
        widget=forms.NumberInput, 
        validators=[MinValueValidator(0)])


