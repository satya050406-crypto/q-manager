from django.db import models
from django.utils.html import format_html
from django.utils.timezone import now

# -------------------------------
# Customer Model
# -------------------------------
class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name


# -------------------------------
# Quotation Model
# -------------------------------
class Quotation(models.Model):
    customer_name = models.CharField(max_length=255)
    quotation_number = models.CharField(max_length=50, unique=True)
    customer_email = models.EmailField(blank=True, null=True)
    customer_phone = models.CharField(max_length=15, blank=True, null=True)

    quotation_pdf = models.FileField(upload_to="quotations/")
    created_at = models.DateTimeField(default=now, editable=False)

    def __str__(self):
        return f"{self.customer_name} - {self.quotation_number}"


# -------------------------------
# PaymentProof Model
# -------------------------------
class PaymentProof(models.Model):
    quotation = models.ForeignKey(
        Quotation, on_delete=models.CASCADE, related_name="proofs"
    )
    image = models.ImageField(upload_to="payment_proofs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def preview(self):
        if self.image:
            return format_html(
                '<img src="{}" width="120" style="border:1px solid #ccc"/>',
                self.image.url
            )
        return "No Image"

    preview.short_description = "Preview"

    def __str__(self):
        return f"Proof for {self.quotation.quotation_number}"


# -------------------------------
# PDF Upload
# -------------------------------
class PDFUpload(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to="uploads/pdfs/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


# -------------------------------
# Screenshot Upload
# -------------------------------
class ScreenshotUpload(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="uploads/screenshots/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

