from django.shortcuts import get_object_or_404, render
from store.models import Product, Category


def home(request, category_slug=None):
    if category_slug != None:
        selected_category = Category.objects.filter(slug = category_slug)
        products = Product.objects.filter(category = selected_category, is_active=True)
        product_count = products.count()
    else:
        products = Product.objects.filter(is_active=True)
        product_count = products.count()

    context ={
        'products': products,
        'product_count': product_count
    }

    return render(request, 'store/home.html', context)
    
	
def product_detail(request, category_slug, product_slug):
    selected_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    context ={
        'product':selected_product
    }
    return render(request, 'store/product_detail.html',context)