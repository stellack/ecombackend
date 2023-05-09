from django.urls import path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('products/', views.productApi),
    path('products/<int:product_id>/', views.productApi),
    path('uploads/',views.SaveFile),

] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 