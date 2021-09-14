from django.urls import path
from . import views


urlpatterns = [
    path('', views.PetList.as_view()),
    (path('<int:pk>/', views.PetDetail.as_view()))
]