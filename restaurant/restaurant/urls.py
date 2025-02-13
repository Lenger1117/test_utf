from django.contrib import admin
from django.urls import path
from food.views import FoodListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/foods/', FoodListView.as_view(), name='food-list'),
]
