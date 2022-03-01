from unicodedata import category
from django.db import models
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500, blank=True)

    def get_url(self):
        return reverse('products_by_category', kwargs={"category_slug": self.slug})

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.PositiveIntegerField()
    images = models.ImageField(upload_to='store/images/product')
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail',kwargs={"category_slug": self.category.slug, "product_slug": self.slug})

    def __str__(self):
        return self.product_name
