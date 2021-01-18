from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)
    total = serializers.SerializerMethodField("get_total")

    def get_total(self, obj):
        items = OrderItem.objects.all().filter(order_id=obj.id)
        return sum((it.price * it.quantity) for it in items)

    class Meta:
        model = Order
        fields = "__all__"
