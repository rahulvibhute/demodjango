
from rest_framework.serializers import ModelSerializer
from myapp.models import *


class LibrarianSer(ModelSerializer):
    class Meta:
        model = Librarian
        fields = '__all__'