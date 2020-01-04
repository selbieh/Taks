from rest_framework.serializers import ModelSerializer
from .models import users



class signUpSerializer(ModelSerializer):
    class Meta:
        model=users
        fields=['email','password']
