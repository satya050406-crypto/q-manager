from django.contrib import admin
from django.urls import path
from quotation import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home + Auth
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),

    # Quotation
    path("upload-quotation/", views.upload_quotation, name="upload_quotation"),
    path("quotations/", views.list_quotations, name="list_quotations"),
    path("quotation/<int:quotation_id>/", views.quotation_detail, name="quotation_detail"),
    path("quotation/<int:quotation_id>/upload-proof/", views.upload_payment_proof, name="upload_payment_proof"),

    # PDFs
    path("upload-pdf/", views.upload_pdf, name="upload_pdf"),
    path("list-pdfs/", views.list_pdfs, name="list_pdfs"),
    path("delete-pdf/<int:pdf_id>/", views.delete_pdf, name="delete_pdf"),

    # Screenshots
    path("upload-screenshot/", views.upload_screenshot, name="upload_screenshot"),
    path("list-screenshots/", views.list_screenshots, name="list_screenshots"),
    path("delete-screenshot/<int:screenshot_id>/", views.delete_screenshot, name="delete_screenshot"),
]

