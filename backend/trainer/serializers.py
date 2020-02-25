from user.serializers import BaseUserSerializer, BaseUserCreateSerializer


class TrainerSerializer(BaseUserSerializer):
    pass


class TrainerCreateSerializer(BaseUserCreateSerializer):

    def create(self, validated_data):
        validated_data['is_trainer'] = True
        return super().create(validated_data)
