from rest_framework import viewsets
from .serializers import CategorySerializer, ProductSerializer, \
                         CustomerSerializer, SportSerializer, TeamSerializer
from .models import Category, Product, Customer, Sport, Team


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all().order_by('sport_name')
    serializer_class = SportSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all().order_by('id')
    serializer_class = TeamSerializer
