from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission

from user.models import User

from . import serializers


class DataOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj


class TrainerCreateView(generics.CreateAPIView):
    serializer_class = serializers.TrainerCreateSerializer


class TrainerRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TrainerSerializer
    queryset = User.objects.filter(is_trainer=True)
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, DataOwner]

