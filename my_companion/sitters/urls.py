from django.urls import path
from sitters import views

urlpatterns = [
    path('sitters/', views.SitterList.as_view()),
    path('sitters/<int:pk>/', views.SitterDetail.as_view())
]
