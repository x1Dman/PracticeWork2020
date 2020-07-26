from django import forms
from .models import ReceiptBoard

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReceiptBoard
        fields = ("name", "email", "text")