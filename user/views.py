from .serializer import signUpSerializer
from rest_framework.generics import CreateAPIView
from  rest_framework.views import APIView
from user.models import users
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


class signUpView(CreateAPIView):
    serializer_class = signUpSerializer
    def post(self, request, *args, **kwargs):
        data=request.data
        validatedUser=signUpSerializer(data=data)
        if validatedUser.is_valid():
            users.objects.create_user(**validatedUser.validated_data)
            return Response({'status':'created','user':validatedUser.data})
        else:
            return Response(validatedUser.errors)


class custumLogIn(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request,username=email, password=password)
        print(user.auth_token)
        if user is not None:
            # token=user.Token.token_key
            # return Response({'token':'token'})
            return Response({'Token': str(user.auth_token)})
        else:
            return Response({'token': 'Not token'})


