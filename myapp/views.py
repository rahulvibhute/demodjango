from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from myapp.models import *
from myapp.serializers import *

# Create your views here.
class LibrarianOp(ModelViewSet):
    queryset = Librarian.objects.all()
    serializer_class = LibrarianSer
