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
