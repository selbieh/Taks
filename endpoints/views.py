
from .models import Metadata, Document
from .serializers import MetadataSerializer, DocumentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions, status, exceptions
from rest_framework.parsers import MultiPartParser, FormParser


class MetadataView(viewsets.ModelViewSet):
    serializer_class = MetadataSerializer
    queryset = Metadata.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name:
            return self.queryset.filter(name=name)
        return self.queryset


class DocumentView(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        if name:
            return self.queryset.filter(name=name)
        return self.queryset

