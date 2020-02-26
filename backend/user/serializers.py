from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

from user.models import User


class BaseUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'slug', 'email', 'is_active', 'is_athlete', 'is_trainer',
            'first_name', 'last_name', 'birthday', 'phone_number',
            'sex', 'city',
        )
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
        read_only_fields = (
            'is_active', 'is_athlete', 'slug', 'is_trainer',
        )


class BaseUserCreateSerializer(BaseUserSerializer):

    class Meta(BaseUserSerializer.Meta):
        fields = [*BaseUserSerializer.Meta.fields, 'password', ]
        extra_kwargs = {
            **BaseUserSerializer.Meta.extra_kwargs,
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['is_active'] = False
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class PasswordForgotSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, data):
        email = data['email']
        user = User.objects.filter(email=email)
        if not user.exists():
            raise serializers.ValidationError(_('User with the given email does not exists.'))
        data['user'] = user.first()
        return data


class PasswordResetSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    password_confirm = serializers.CharField(required=True)

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError(_('The two password fields didn’t match.'))
        return data
