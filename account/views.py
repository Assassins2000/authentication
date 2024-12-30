from .models import User

from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import UserSerializer, GetTokenSerializer
from .models import User, UserExistsException

class AccountViewSet(viewsets.ViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        return super().get_permissions()

    def create(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"status": 200, "message": 'success'})
        except UserExistsException:
               return Response({"status": 400, "message": "User exists"})


    @action(detail=False, methods=['post'])
    def get_access_token(self, request):
         serializer = GetTokenSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         token, user = serializer.save()
         return Response({
              "user": UserSerializer(user).data,
              "token": token.key
         })
    
    @action(detail=False, methods=['get'], permission_classes= [permissions.IsAuthenticated])
    def me(self, request):
        return Response({'user': UserSerializer(request.user).data})
    