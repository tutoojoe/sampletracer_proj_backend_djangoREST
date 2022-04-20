from django.shortcuts import render
from products.models import Style
from products.serializers import StyleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404

from products.serializers import StyleDetailedSerializer, StyleCreateSerializer
# Create your views here.


class StylesListView(generics.ListCreateAPIView):
    """
    Lists out all the styles 
    """
    queryset = Style.objects.all()
    serializer_class = StyleCreateSerializer

    # class StylesListView(APIView):
    #     def get(self, request, format=None):
    #         styles = Style.objects.all()
    #         serializer = StyleSerializer(styles, many=True)
    #         return Response(serializer.data)

    #     def post(self, request, format=None):

    #         serializer = StyleSerializer(data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data, status=status.HTTP_201_CREATED)
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
