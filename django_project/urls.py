"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Ticket URLS will be at /projects since that is the outer model
    path("projects/", include("tickets.urls")),
    # Adminlte2 default routes for demo purpose
    path("", include("adminlte2_pdq.urls")),
    # Django Account Routes
    path("accounts/", include("django.contrib.auth.urls")),
    # Admin - Styled in Django but hosted in Adminlye2 layout
    path("admin/", admin.site.urls),
]
