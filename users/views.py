from rest_framework.views import APIView
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class Signup(APIView):
    def get(self, request):
        return Response({"message": "이름,이메일,비밀번호,생일을 입력해주세요."})

    def post(self, request):
        
        password = request.data.get("password")
        
        if not password or len(password) < 8:
            return Response({"message": "비밀번호는 8자 이상이어야합니다."})
        serializer = UserSerializer(data=request.data)
        
        
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        

class Login(APIView):
    pass