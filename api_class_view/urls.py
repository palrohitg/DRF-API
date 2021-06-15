from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.BlogList.as_view()), 
    path('<int:pk>/', views.BlogDetails.as_view()),
]
