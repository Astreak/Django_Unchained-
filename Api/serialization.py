from rest_framework import serializers
from .models import Author

class ApiCreation(serializers.HyperlinkedModelSerializer):
    class  Meta:
        model=Author
        fields=('id','name','book')