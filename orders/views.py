import csv

from django.http import HttpResponse

from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser

from admin.pagination import CustomPagination
from users.authentication import JWTAuthentication
from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrderGenericAPIView(
    generics.GenericAPIView, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    pagination_class = CustomPagination

    def get(self, request, pk=None):
        if pk:
            return Response({"data": self.retrieve(request, pk).data})

        return self.list(request)


class ExportAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = "attachment: filename=orders.csv"

        orders = Order.objects.all()
        writer = csv.writer(response)

        writer.writerow(["ID", "Name", "Email", "Product Title", "Price", "Quantity"])

        for order in orders:
            writer.writerow([order.id, order.name, order.email, "", "", ""])

            order_items = OrderItem.objects.all().filter(order_id=order.id)

            for item in order_items:
                writer.writerow(
                    ["", "", "", item.product_title, item.price, item.quantity]
                )

        return response
