from django.urls import path
from . import views

urlpatterns = [
    path('',views.SoftwareListView.as_view())
]