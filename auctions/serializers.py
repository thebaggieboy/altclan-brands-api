from rest_framework import serializers

from .models import Auctions



class AuctionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auctions
        fields = ['product_name', 'product_description', 'display_image', 'highest_bid', 'current_date', 'start_date', 'end_date']
