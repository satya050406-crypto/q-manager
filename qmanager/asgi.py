# qmanager/urls.py

from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from quotation import views

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),

    # Home / Dashboard
    path("", views.home, name="home"),

    # Auth
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # Uploads
    path("upload/pdf/", views.upload_pdf, name="upload_pdf"),
    path("upload/screenshot/", views.upload_screenshot, name="upload_screenshot"),

    # Lists
    path("pdfs/", views.list_pdfs, name="list_pdfs"),
    path("screenshots/", views.list_screenshots, name="list_screenshots"),

    # Deletes
    path("delete/pdf/<int:pk>/", views.delete_pdf, name="delete_pdf"),
    path("delete/screenshot/<int:pk>/", views.delete_screenshot, name="delete_screenshot"),
]

# Static + Media
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)