from django.urls import path
from clients import views

urlpatterns = [
    path('clients/', views.ClientList.as_view()),
    path('clients/<int:pk>/', views.ClientDetail.as_view())
]
