from rest_framework.serializers import ModelSerializer, CharField, SerializerMethodField
from django.contrib.auth.models import User
from .models import  Ticket


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "password"]

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            is_staff=False,
            is_superuser=False
        )

        user.set_password(validated_data['password'])
        user.save()
        return user


class TicketSerializer(ModelSerializer):
    user_name = SerializerMethodField()
    user_id = SerializerMethodField(read_only=True)
    def get_user_name(self,obj):
        return obj.user.username

    def get_user_id(self,obj):
        return obj.user.id

    class Meta:
        model = Ticket
        fields = ['id','issue','priority','user_name',"user_id"]