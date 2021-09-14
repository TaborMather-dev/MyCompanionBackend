from django.urls import path
from . import views


urlpatterns = [
    path('', views.SitterList.as_view()),
    (path('<int:pk>/', views.SitterDetail.as_view()))
]
