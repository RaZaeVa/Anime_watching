from rest_framework import serializers
from .models import User
from apps.content.serializers import WatchHistorySerializer


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('phone_number', 'username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password': 'Password fields do not match'})
        user = User.objects.create_user(password=password, **validated_data)
        return user

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    latest_watch = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'latest_watch')

    def get_latest_watch(self, user):
        # Получаем последние три аниме для данной категории
        latest_watch = user.watchhistory_set.order_by('-watched_at')[:3]
        # Сериализуем аниме
        serializer = WatchHistorySerializer(latest_watch, many=True)
        return serializer.data