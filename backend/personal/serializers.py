from rest_framework import serializers

from personal.models import Personal


class PersonalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personal
        fields = ['id', 'user.first_name', 'users', 'created']
