from django.urls import path
from . import views


urlpatterns = [
    path('status/', views.Status.as_view(), name='status'),]