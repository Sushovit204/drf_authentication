from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime, os
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()
secret = os.getenv('secret_key')


class RegisterView(APIView):
    """View for registering the user"""
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class LoginView(APIView):
    """View for loging th user"""
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            raise AuthenticationFailed('User Not Found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect Password')
        
        payload = {
            'id':user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow(),
        }

        token = jwt.encode(payload, secret , algorithm='HS256')

        respose = Response()

        respose.set_cookie(key='jwt', value=token, httponly=True)
        respose.data = {
            'jwt':token,
        }
        
        return respose
    

class UserView(APIView):
    """view to get user via cookie"""
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed("Unauthorized Access!")
        
        try:
            payload = jwt.decode(token, secret, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Session Expired!")
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)