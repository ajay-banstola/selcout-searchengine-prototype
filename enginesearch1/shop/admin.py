from django.contrib import admin
from .models import Category, Product, Mixture


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created_at', 'updated_at']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ["category__name", "description", "url"]


admin.site.register(Product, ProductAdmin)


#class MixtureAdmin(admin.ModelAdmin):
#    list_display = ['name', 'slug', 'price', 'stock']
    #list_filter = ['available']
#    list_editable = ['price', 'stock']
#    prepopulated_fields = {'slug': ('name',)}


#admin.site.register(Mixture, MixtureAdmin)
