from rest_framework import serializers

from .models import Communities



class CommunitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Communities
        fields = ['community_name', 'community_type', 'community_description', 'display_image', ]
