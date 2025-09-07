from django.contrib import admin
from .models import Customer, Quotation, PaymentProof


# -------------------------------
# Customer Admin
# -------------------------------
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "email")


# -------------------------------
# PaymentProof Inline (for Quotation)
# -------------------------------
class PaymentProofInline(admin.TabularInline):   # StackedInline bhi use kar sakta hai
    model = PaymentProof
    extra = 3   # default 3 slots
    readonly_fields = ('uploaded_at', 'preview')


# -------------------------------
# Quotation Admin
# -------------------------------
@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ('quotation_number', 'customer_name', 'created_at')
    search_fields = ('quotation_number', 'customer_name')
    inlines = [PaymentProofInline]


