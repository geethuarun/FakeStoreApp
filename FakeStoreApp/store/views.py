from django.shortcuts import render

# Create your views here.

from rest_framework.viewsets import ModelViewSet

from store.serializers import CategorySerializer
from store.models import Category

class CategoryView(ModelViewSet):
    serializer_class=CategorySerializer
    queryset=Category.objects.all()
    #   @action(method=["delete"],detail=True)
    # def remove_category(request,*args,**kwargs):
    # id=kwargs.get("pk")
    # Category.objects.filter(id=id).update(is_active=False)
    
    # return Response

