# from django.contrib import admin
from django.urls import path
from . import views
from accounts.views import SignUpView
#
urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signupPage'),
    ]