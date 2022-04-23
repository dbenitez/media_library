from django.test import TestCase
from django.urls import resolve
from ..views import VendorListView

class VendorsTests(TestCase):
    def test_vendor_url_resolves_vendor_view(self):
        view = resolve("sofware/vendor/")
        self.assertEquals(view.func.view_class, VendorListView)