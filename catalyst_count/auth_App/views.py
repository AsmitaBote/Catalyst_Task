from rest_framework.generics import CreateAPIView
from .serializer import UserSerializer

class UserAPI(CreateAPIView):
    serializer_class = UserSerializer

