from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FoodCategory
from .models import FoodListSerializer

class FoodListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = FoodCategory.objects.filter(
            food__is_publish=True
        ).distinct().order_by('order_id', 'name_ru')

        serializer = FoodListSerializer(categories, many=True)
        return Response(serializer.data)