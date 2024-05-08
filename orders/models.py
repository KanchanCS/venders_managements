from django.db import models

from vendors.models import Vendor
from django.utils import timezone
# Create your models here.


class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=20, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=20)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    acknowledged = models.BooleanField(default=False)

    def acknowledge(self):
        if not self.acknowledged:
            self.acknowledged = True
            self.acknowledgment_date = timezone.now()
            self.save()

    def calculate_performance_metrics(self):
        # On-Time Delivery Rate
        completed_orders = PurchaseOrder.objects.filter(
            vendor=self.vendor, status="completed"
        )
        on_time_delivery_orders = completed_orders.filter(
            delivery_date__lte=timezone.now()
        )
        self.vendor.on_time_delivery_rate = (
            (on_time_delivery_orders.count() / completed_orders.count()) * 100
            if completed_orders.count() != 0
            else 0
        )

        # Quality Rating Average
        completed_orders_with_rating = completed_orders.exclude(
            quality_rating__isnull=True
        )
        quality_ratings = completed_orders_with_rating.values_list(
            "quality_rating", flat=True
        )
        self.vendor.quality_rating = (
            sum(quality_ratings) / completed_orders_with_rating.count()
            if completed_orders_with_rating.count() != 0
            else 0
        )

        # Average Response Time
        acknowledged_orders = completed_orders.filter(acknowledged=True)
        response_times = [
            (po.acknowledgment_date - po.issue_date).total_seconds() / 3600
            for po in acknowledged_orders
        ]
        self.vendor.response_time = (
            sum(response_times) / len(response_times) if len(response_times) != 0 else 0
        )

        # Fulfilment Rate
        fulfilled_orders = completed_orders.filter(status="completed")
        self.vendor.fulfilment_rate = (
            (
                fulfilled_orders.count()
                / PurchaseOrder.objects.filter(vendor=self.vendor).count()
            )
            * 100
            if PurchaseOrder.objects.filter(vendor=self.vendor).count() != 0
            else 0
        )

        # Save the updated vendor metrics
        self.vendor.save()
