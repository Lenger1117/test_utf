from django.contrib import admin
from .models import FoodCategory, Food

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ru', 'name_en', 'name_ch', 'order_id')
    search_fields = ('name_ru', 'name_en', 'name_ch')
    ordering = ('order_id', 'name_ru')

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = (
        'internal_code', 'code', 'name_ru', 'description_ru', 'is_vegan',
        'is_special', 'cost', 'category', 'is_publish'
    )
    search_fields = ('name_ru', 'description_ru', 'category__name_ru')
    list_filter = ('is_vegan', 'is_special', 'is_publish', 'category')
    ordering = ('internal_code', 'name_ru')