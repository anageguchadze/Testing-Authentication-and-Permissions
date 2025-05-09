from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import PrivateItem
from .serializers import PrivateItemSerializer

class PrivateItemViewSet(viewsets.ModelViewSet):
    queryset = PrivateItem.objects.all()
    serializer_class = PrivateItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
