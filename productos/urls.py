# productos/urls.py
from django.urls import path
from .views import ProductListView

urlpatterns = [
path('productos/', ProductListView.as_view(), name='product_list'),
]
