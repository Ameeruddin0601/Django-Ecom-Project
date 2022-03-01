from django.contrib import admin
from store import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('product_name',)}

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('category_name',)}