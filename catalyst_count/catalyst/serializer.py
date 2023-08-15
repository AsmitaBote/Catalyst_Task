from rest_framework import serializers
from .models import UpdateDataModel, QueryBuilderModel

class UploadDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdateDataModel
        fields = '__all__'

class QueryBuilderSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueryBuilderModel
        fields = '__all__'
