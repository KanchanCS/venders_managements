# views.py
from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer, VendorPerformanceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.reverse import reverse


class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class VendorPerformanceAPIView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = Vendor.objects.get(pk=vendor_id)
            serializer = VendorPerformanceSerializer(vendor)
            return Response(serializer.data)
        except Vendor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class APIRootView(viewsets.ViewSet):
    def list(self, request, format=None):
        # Generate a list of all available API endpoints
        endpoints = {
            "vendors": reverse(
                "vendors:vendor-list-create", request=request, format=format
            ),
            "purchase_orders": reverse(
                "orders:purchase-order-list-create", request=request, format=format
            ),
            # Add other API endpoints here
        }
        return Response(endpoints)
