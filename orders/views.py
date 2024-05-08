from rest_framework import generics
from .models import PurchaseOrder
from .serializers import PurchaseOrderSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class AcknowledgePurchaseOrderAPIView(APIView):
    def post(self, request, id):
        try:
            purchase_order = PurchaseOrder.objects.get(pk=id)
            purchase_order.acknowledge()  # Mark the purchase order as acknowledged
            purchase_order.calculate_performance_metrics()  # Recalculate average_response_time
            return Response(status=status.HTTP_200_OK)
        except PurchaseOrder.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        return Response(status=status.HTTP_200_OK)
