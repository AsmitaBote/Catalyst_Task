from django.urls import path
from .views import UploadDataViewSet, QueryBuilderViewSet

urlpatterns = [
    path('upload/', UploadDataViewSet.as_view(), name='upload_url'),
    path('query/', QueryBuilderViewSet.as_view(), name='query_url')
]