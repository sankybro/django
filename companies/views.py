from django.shortcuts import render
from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import stock
from .serializers import stockSerializer
from django.shortcuts import get_object_or_404
# Create your views here.

class StockList(APIView):

    def get(self , request):
        stocks = stock.objects.all()
        serializer = stockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self):
        pass