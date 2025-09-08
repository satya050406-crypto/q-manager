from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from quotation import views  # ye rakho agar sab views quotation app me hain

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # Home + Auth
    path("", views.home, name="home"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),

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

