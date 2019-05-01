from rest_framework import serializers
from .models import stock

class stockSerializer(serializers.ModelSerializer):

    class meta:
        model = stock
        fields = '__all__'
