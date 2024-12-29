from .models import User

from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer
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
