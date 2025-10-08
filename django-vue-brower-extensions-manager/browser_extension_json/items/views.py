from django.shortcuts import render

from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows items to be viewed or edited.
    """
    queryset = Item.objects.all().order_by('-created_at')
    serializer_class = ItemSerializer
 Create your views here.
