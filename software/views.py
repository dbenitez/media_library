from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SoftwareListView(TemplateView):
    template_name = 'software/list.html'