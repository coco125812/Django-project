from django.contrib import admin
from .models import Products, Order

# Register your models here.
admin.site.site_header ="E-commerce Site"
admin.site.site_title="ecom site"
admin.site.index_title="manage shopping"

# class ProductAdmin(admin, ModelAdmin):
#     list_display = ('title','price','discount_price','category','image')
admin.site.register(Products,)
admin.site.register(Order)