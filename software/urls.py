from django.urls import path
from . import views

app_name = "software"

urlpatterns = [
    path('',views.SoftwareListView.as_view()),
    path('vendor/',views.VendorListView.as_view(), name="vendor_list"),
    path('vendor/<pk>/update/', views.VendorUpdateView.as_view(), name="vendor_update"),
    path('vendor/create/', views.VendorCreateView.as_view(), name="vendor_create")
]