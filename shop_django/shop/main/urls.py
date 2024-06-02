from django.urls import path
from .views import ProductListView, ProductDetailView

urlpatterns = [
    path('', ProductDetailView.as_view(), name='products-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
