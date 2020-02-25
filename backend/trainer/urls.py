from django.urls import path

from . import views


urlpatterns = [
    path('', views.TrainerCreateView.as_view(), name='trainer-list-create'),
    path('<str:slug>/', views.TrainerRetrieveUpdateView.as_view(), name='trainer-detail-update-delete'),

]
