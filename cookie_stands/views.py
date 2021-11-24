from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieStandSerializer


class CookieStandsList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer


class CookieStandsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieStandSerializer
