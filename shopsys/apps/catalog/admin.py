#-*-coding:utf8-*-
from django.contrib import admin
from .models import Category, Product
from .forms import ProductAdminForm

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
     #设置admin页面的列表展示
    form = ProductAdminForm
    list_display = ('name', 'price', 'old_price', 'created_at', 'updated_at', )
    list_display_links = ('name', )
    list_per_page = 50
    ordering = ['-created_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
     #除了以下的都显示，对应的field显示哪个，或者不写就都显示
    exclude = ('created_at', 'updated_at')
     #根据name自动填充 转换关系 可以在界面使用
    prepopulated_fields = {'slug':('name', )}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    #设置admin页面的列表展示
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name', )
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    exclude = ('created_at', 'updated_at')
    prepopulated_fields = {'slug':('name', )}
