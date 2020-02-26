from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, BasePermission

from user.models import User
from user.tokens import account_activation_token
from utils.emails import Email

from . import serializers


class DataOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        user = request.user
        return user == obj


class TrainerCreateView(generics.CreateAPIView):
    serializer_class = serializers.TrainerCreateSerializer

    def perform_create(self, serializer):
        trainer = serializer.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Activate your account.'
        message = render_to_string('trainer_active_email.html', {
            'trainer': trainer,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(trainer.pk)),
            'token': account_activation_token.make_token(trainer),
        })
        to_email = trainer.email
        email = Email(
            mail_subject, message, to=[to_email]
        )
        email.send()


class TrainerRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.TrainerSerializer
    queryset = User.objects.filter(is_trainer=True)
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, DataOwner]

