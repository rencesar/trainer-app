from django.urls import path

from . import views


urlpatterns = [
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('reset-password/<uidb64>/<token>/', views.reset_password, name='reset-password'),
    path('activate-account/<uidb64>/<token>/', views.activate_account, name='activate-account'),

]
