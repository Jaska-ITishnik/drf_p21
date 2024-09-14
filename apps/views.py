from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.filters import SearchFilter
from rest_framework.generics import RetrieveUpdateDestroyAPIView, GenericAPIView, ListCreateAPIView, CreateAPIView

from apps.filters import ProductFilterSet, CategoryFilterSet
from apps.models import Category, Product, User
from apps.serializers import CategoryModelSerializer, ProductModelSerializer, RegisterModelSerializer


class RetrieveCreateUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView, mixins.CreateModelMixin, GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    filter_backends = DjangoFilterBackend,
    filterset_class = CategoryFilterSet


class ProductListCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = SearchFilter, DjangoFilterBackend
    # filterset_fields = 'category', 'id' # basic version of filter
    filterset_class = ProductFilterSet
    search_fields = 'name',
    # permission_classes = IsAuthenticated,


class RegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterModelSerializer