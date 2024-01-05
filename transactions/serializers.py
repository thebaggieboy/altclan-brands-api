from rest_framework import serializers

from .models import *
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['order_date',  'name_of_item',  'user_email',  'name_of_brand', 'amount_per_item', 'quantity', 'tracking_number', 'number_of_items', 'address', 'ordered', 'delivered']



class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = [ 'user_email', 'full_name', 'paystack_charge_id',  'amount', 'status', 'timestamp']


class CouponSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coupon
        fields = [ 'code', 'amount']



class RefundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Refund
        fields = [ 'order', 'reason', 'accepted', 'email' ]



