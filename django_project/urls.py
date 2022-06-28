# django_project/urls.py
from django.contrib import admin
from django.urls import path, include  # new

urlpatterns = [
    #path("google/", "pages.urls"),
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),  # new
]