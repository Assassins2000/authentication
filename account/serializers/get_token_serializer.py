from rest_framework import exceptions, serializers
from datetime import datetime
from account.models import User, CustomToken, UserExistsException 

class GetTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length = 32, write_only = True)

    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data["email"])
            
            if not user.check_password(validated_data["password"]):
                raise exceptions.AuthenticationFailed('Unable to log in with provided credentials.')
            
            token = CustomToken.objects.create(user=user)
            return token, user
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('Unable to log in with provided credentials.')