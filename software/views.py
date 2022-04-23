from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView

from software.models import Vendor

# Create your views here.
class SoftwareListView(TemplateView):
    template_name = 'software/list.html'


class VendorListView(ListView):
    model = Vendor
    context_object_name = 'vendor_list'
    template_name = 'sofware/vendor_list.html'

class VendorCreateView(CreateView):
    model=Vendor
    fields=["name", "website", "logo"]
    success_url = "/software/vendor/"

class VendorUpdateView(UpdateView):
    model=Vendor
    fields=["name", "website", "logo"]
    success_url = "/software/vendor/"