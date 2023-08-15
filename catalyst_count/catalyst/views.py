from rest_framework import viewsets
from .serializer import UploadDataSerializer, QueryBuilderSerializer
from .models import UpdateDataModel, QueryBuilderModel
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UploadDataViewSet(viewsets.ModelViewSet):
    serializer_class = UploadDataSerializer
    queryset = UpdateDataModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class QueryBuilderViewSet(viewsets.ModelViewSet):
    serializer_class = QueryBuilderSerializer
    queryset = QueryBuilderModel.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]