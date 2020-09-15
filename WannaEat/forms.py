from django import forms
from .models import ReceiptBoard

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReceiptBoard
        fields = ("name", "email", "text")

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()