from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Quotation, PaymentProof, PDFUpload, ScreenshotUpload
from .forms import QuotationForm, PaymentProofForm, PDFUploadForm, ScreenshotUploadForm


# -------------------------------
# HOME
# -------------------------------
def home(request):
    return HttpResponse("Hello! Qmanager app is working 🚀")


# -------------------------------
# LOGIN VIEW
# -------------------------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")


# -------------------------------
# LOGOUT VIEW
# -------------------------------
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")


# -------------------------------
# UPLOAD QUOTATION
# -------------------------------
@login_required
def upload_quotation(request):
    if request.method == "POST":
        form = QuotationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Quotation uploaded successfully.")
            return redirect("list_quotations")
    else:
        form = QuotationForm()
    return render(request, "upload_quotation.html", {"form": form})


# -------------------------------
# LIST QUOTATIONS
# -------------------------------
@login_required
def list_quotations(request):
    quotations = Quotation.objects.all()
    return render(request, "list_quotations.html", {"quotations": quotations})


# -------------------------------
# QUOTATION DETAIL (with proofs)
# -------------------------------
@login_required
def quotation_detail(request, quotation_id):
    quotation = get_object_or_404(Quotation, id=quotation_id)
    proofs = quotation.proofs.all()
    return render(
        request,
        "quotation_detail.html",
        {"quotation": quotation, "proofs": proofs}
    )


# -------------------------------
# UPLOAD PAYMENT PROOF
# -------------------------------
@login_required
def upload_payment_proof(request, quotation_id):
    quotation = get_object_or_404(Quotation, id=quotation_id)
    if request.method == "POST":
        form = PaymentProofForm(request.POST, request.FILES)
        if form.is_valid():
            proof = form.save(commit=False)
            proof.quotation = quotation
            proof.save()
            messages.success(request, "Payment proof uploaded successfully.")
            return redirect("quotation_detail", quotation_id=quotation.id)
    else:
        form = PaymentProofForm()
    return render(
        request,
        "upload_payment_proof.html",
        {"form": form, "quotation": quotation}
    )


# -------------------------------
# UPLOAD PDF (PDFUpload model)
# -------------------------------
@login_required
def upload_pdf(request):
    if request.method == "POST":
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "PDF uploaded successfully.")
            return redirect("list_pdfs")
    else:
        form = PDFUploadForm()
    return render(request, "upload_pdf.html", {"form": form})


# -------------------------------
# LIST PDFs
# -------------------------------
@login_required
def list_pdfs(request):
    pdfs = PDFUpload.objects.all()
    return render(request, "list_pdfs.html", {"pdfs": pdfs})


# -------------------------------
# UPLOAD SCREENSHOT (ScreenshotUpload model)
# -------------------------------
@login_required
def upload_screenshot(request):
    if request.method == "POST":
        form = ScreenshotUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Screenshot uploaded successfully.")
            return redirect("list_screenshots")
    else:
        form = ScreenshotUploadForm()
    return render(request, "upload_screenshot.html", {"form": form})


# -------------------------------
# LIST Screenshots
# -------------------------------
@login_required
def list_screenshots(request):
    screenshots = ScreenshotUpload.objects.all()
    return render(request, "list_screenshots.html", {"screenshots": screenshots})

from django.contrib.auth.decorators import login_required

@login_required
def delete_pdf(request, pdf_id):
    pdf = get_object_or_404(PDFUpload, id=pdf_id)
    pdf.delete()
    messages.success(request, "PDF deleted successfully.")
    return redirect("list_pdfs")

@login_required
def delete_screenshot(request, screenshot_id):
    screenshot = get_object_or_404(ScreenshotUpload, id=screenshot_id)
    screenshot.delete()
    messages.success(request, "Screenshot deleted successfully.")
    return redirect("list_screenshots")

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.user.is_superuser:
        role = "Admin"
    elif request.user.is_staff:
        role = "Staff"
    else:
        role = "Normal User"
    
    return render(request, "dashboard.html", {"role": role})
