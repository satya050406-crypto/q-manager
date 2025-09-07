from django import forms
from .models import Quotation, PaymentProof


class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['customer_name', 'quotation_number', 'customer_email', 'customer_phone', 'quotation_pdf']


class PaymentProofForm(forms.ModelForm):
    class Meta:
        model = PaymentProof
        fields = ['quotation', 'image']

from .models import Quotation, PaymentProof, PDFUpload, ScreenshotUpload

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = ['customer_name', 'quotation_number', 'customer_email', 'customer_phone', 'quotation_pdf']


class PaymentProofForm(forms.ModelForm):
    class Meta:
        model = PaymentProof
        fields = ['quotation', 'image']


class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = PDFUpload
        fields = ['title', 'file']


class ScreenshotUploadForm(forms.ModelForm):
    class Meta:
        model = ScreenshotUpload
        fields = ['title', 'image']
