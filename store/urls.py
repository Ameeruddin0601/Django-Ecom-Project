from django.urls import path
from store import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:category_slug>/', views.home, name='products_by_category'),
    path('<slug:category_slug>/<product_slug>/', views.product_detail, name='product_detail')
] 