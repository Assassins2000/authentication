from rest_framework import serializers
from users.models import User, UserExistsException 

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length = 100)
    last_name = serializers.CharField(max_length = 100)
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 32, write_only = True)

    def create(self, validated_data):
        user = User.objects.create_user(email = validated_data['email'],
                                        first_name = validated_data['first_name'],
                                        last_name = validated_data['last_name'],
                                        password = validated_data['password'])
        return user