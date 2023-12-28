from rest_framework import serializers

from .models import *
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['order_date', 'tracking_number', 'number_of_items', 'ordered', 'delivered']



class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = [  'amount', 'status', 'timestamp']


class CouponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coupon
        fields = [ 'code', 'amount']



class RefundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Refund
        fields = [ 'order', 'reason', 'accepted', 'email' ]



