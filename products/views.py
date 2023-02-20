from django.core import serializers
from django.db.models import Q
from django.shortcuts import get_object_or_404, get_list_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *

# Create your views here.

@api_view(['GET', 'POST'])
def SearchboxView (request):
    child1 = request.data.get('child1')
    child2 = request.data.get('child2')
    child3 = request.data.get('child3')
    name = request.data.get('name')
    color = request.data.get('color')
    size = request.data.get('size')
    material = request.data.get('material')
    products = get_list_or_404(Products)
    if products:
        products = Products.objects.all()
        if child1 :
            products = products.filter(child1__id=child1)
            if child2:
                products = products.filter(child2__id=child2)
                if child3:
                    products = products.filter(child3__id=child3)
        if name: 
            products = products.filter(name__icontains=name)
        if color:
            products = products.filter(color__id=color)
        if size:
            products = products.filter(size__id=size)
        if material:
            products = products.filter(material__id=material)

    product_list = serializers.serialize("python", products)
    return Response(product_list)

# products.filter(user__category_id=category_id).prefetch_related(Prefetch('user_set', queryset=colors))

# @api_view(['GET', 'POST'])
# def SearchboxView (request):
#     name = request.data.get('name')
#     products = get_list_or_404(Products)
#     product_list = serializers.serialize("python", products)
#     return Response(product_list)








