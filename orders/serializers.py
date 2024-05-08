from rest_framework import serializers
from .models import PurchaseOrder


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = [
            "id",
            "po_number",
            "vendor",
            "issue_date",
            "order_date",
            "delivery_date",
            "items",
            "quantity",
            "status",
            "acknowledged",
            "acknowledgment_date",
        ]
