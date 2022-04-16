"""cvmarket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.urls import path
from django.urls import path

import authentication.views
import cvblog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cvblog.views.accueil, name='accueil'),
    path('cv_admin/<int:cv_id>', cvblog.views.view_cv_admin, name='view_cv_admin'),
    path('login', LoginView.as_view(
        template_name='authentication/login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/', PasswordChangeView.as_view(
        template_name='authentication/password_change_form.html'),
         name='password_change'
         ),
    path('change-password-done/', PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'),
         name='password_change_done'
         ),
    path('signup/', authentication.views.signup_page, name='signup'),
    path('profile-photo/upload', authentication.views.upload_profile_photo,
         name='upload_profile_photo'),
    path('profile/upload', authentication.views.upload_profile,
         name='upload_profile'),
    path('home/', cvblog.views.home, name='home'), 
    path('cv-feed/', cvblog.views.cv_feed, name='cv_feed'),
    path('lettre-feed/', cvblog.views.lettre_feed, name='lettre_feed'),
    path('cv/create', cvblog.views.cv_upload, name='cv_create'),
    path('lettre/create', cvblog.views.lettre_upload, name='lettre_create'),
    path('cv/<int:cv_id>', cvblog.views.view_cv, name='view_cv'),
    path('lettre/<int:lettre_id>', cvblog.views.view_lettre, name='view_lettre'),
    path('cv/<int:cv_id>/edit', cvblog.views.edit_cv, name='edit_cv'),
    path('lettre/<int:lettre_id>/edit', cvblog.views.edit_lettre, name='edit_lettre'),
    path('contact/', cvblog.views.contact, name='contact'),
    path('contact/<int:contact_id>/edit', cvblog.views.edit_contact,name='edit_contact'),
    path('cvpdf/<int:cv_id>', cvblog.views.some_view_cv, name='some_view_cv'),
    path('cvlettre/<int:lettre_id>', cvblog.views.some_view_lettre, name='some_view_lettre'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

