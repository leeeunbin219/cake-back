from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from .serializers import SignupSerializer


class Signup(APIView):
    def get(self, request):
        return Response({"message": "이름,닉네임,이메일,비밀번호,생일을 입력해주세요."})

    def post(self, request):
        
        password = request.data.get("password")
        
        if not password or len(password) < 8:
            return Response({"message": "비밀번호는 8자 이상이어야합니다."})
        serializer = SignupSerializer(data=request.data)
        
        
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = SignupSerializer(user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        

class Login(APIView):
    
    def get(self, request):
        return Response({"message": "이메일, 비밀번호를 입력해주세요."})
    
    def post(self,request):
        
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "로그인 성공"}, status=HTTP_200_OK)
        else:
            return Response({"message": "이메일, 비밀번호를 확인해주세요."}, status=HTTP_400_BAD_REQUEST)
        
        
class Logout(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        logout(request)
        return Response({"message": "로그아웃 되었습니다."}, status=HTTP_200_OK)