from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_general, name="info_general"),
    path('<int:info_id>/', views.info_details, name="info_details"),
]
