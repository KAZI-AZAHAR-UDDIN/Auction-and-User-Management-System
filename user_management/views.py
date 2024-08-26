from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, get_user_model
from .serializers import UserSerializer, LoginSerializer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

User = get_user_model()

# User Registration
@method_decorator(csrf_exempt, name='dispatch')  # Temporarily disabling CSRF for testing
class UserRegisterView(APIView):
    permission_classes = [AllowAny]  # This allows access without authentication

    def post(self, request):
        print("Received request data:", request.data)  # Debugging: Log request data
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print("User created successfully:", serializer.data)  # Debugging: Log success
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print("Validation errors:", serializer.errors)  # Debugging: Log validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login with JWT Token
@method_decorator(csrf_exempt, name='dispatch')  # Temporarily disabling CSRF for testing
class UserLoginView(APIView):
    permission_classes = [AllowAny]  # This allows access without authentication

    def post(self, request):
        print("Received login data:", request.data)  # Debugging: Log request data
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                print("Login successful for user:", username)  # Debugging: Log success
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            print("Invalid credentials for user:", username)  # Debugging: Log invalid credentials
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        print("Login validation errors:", serializer.errors)  # Debugging: Log validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
