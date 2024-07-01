from django.urls import path
from . import views

urlpatterns = [
    path('', views.budget_list, name='budget_list'),
    path('budget/<int:pk>/', views.budget_detail, name='budget_detail'),
    path('budget/new/', views.budget_create, name='budget_create'),
    path('budget/<int:pk>/edit/', views.budget_update, name='budget_update'),
    path('budget/<int:pk>/delete/', views.budget_delete, name='budget_delete'),
]
