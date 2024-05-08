# urls.py
from django.urls import path
from .views import (
    VendorListCreateAPIView,
    VendorPerformanceAPIView,
    VendorRetrieveUpdateDestroyAPIView,
)

app_name = "vendors"

urlpatterns = [
    path("/", VendorListCreateAPIView.as_view(), name="vendor-list-create"),
    path(
        "/<int:pk>/",
        VendorRetrieveUpdateDestroyAPIView.as_view(),
        name="vendor-retrieve-update-destroy",
    ),
    path("/<int:vendor_id>/performance", VendorPerformanceAPIView.as_view()),
]
