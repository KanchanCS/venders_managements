from django.urls import path
from .views import (
    AcknowledgePurchaseOrderAPIView,
    PurchaseOrderListCreateAPIView,
    PurchaseOrderRetrieveUpdateDestroyAPIView,
)

app_name = "orders"

urlpatterns = [
    path(
        "",
        PurchaseOrderListCreateAPIView.as_view(),
        name="purchase-order-list-create",
    ),
    path(
        "/<int:pk>/",
        PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(),
        name="purchase-order-retrieve-update-destroy",
    ),
    path(
        "/<int:id>/acknowledge",
        AcknowledgePurchaseOrderAPIView.as_view(),
    ),
]
