from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.productApi),
    path('products/<int:product_id>/', views.productApi),

]