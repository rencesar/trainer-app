from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from user import serializers
from user.models import User
from user.tokens import account_activation_token, reset_password_token
from utils.emails import Email


class IsNotAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        return bool(not request.user or not request.user.is_authenticated)


def get_user_from_uidb64(uidb64):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    return user


@api_view(['POST'])
@permission_classes([IsNotAuthenticated])
def forgot_password(request):
    serializer = serializers.PasswordForgotSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    current_site = get_current_site(request)
    mail_subject = 'Forgot your password.'
    message = render_to_string('forgot_password_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': reset_password_token.make_token(user),
    })
    to_email = user.email
    email = Email(
        mail_subject, message, to=[to_email]
    )
    email.send()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsNotAuthenticated])
def reset_password(request, uidb64, token):
    user = get_user_from_uidb64(uidb64)
    if user is not None and reset_password_token.check_token(user, token):
        serializer = serializers.PasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user.set_password(serializer.validated_data['password'])
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def activate_account(request, uidb64, token):
    user = get_user_from_uidb64(uidb64)
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
