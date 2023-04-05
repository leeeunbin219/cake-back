from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import SignupSerializer, UserDetailSerializer, UserSerializer
from .models import User


# 케이크 주인 회원가입
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


# 유저 정보 조회 및 수정 삭제 (user용)
class Mypage(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({"message": "계정이 삭제되었습니다."}, status=HTTP_204_NO_CONTENT)


# 유저 정보 자세히 조회(admin용)
class UserDetail(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise NotFound(status=HTTP_400_BAD_REQUEST)

        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserDetailSerializer(
            user,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            user = serializer.save()
            serializer = UserDetailSerializer(user)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response({"message": "계정이 삭제되었습니다."}, status=HTTP_200_OK)


# 케이크 주인 로그인
class Login(APIView):
    def get(self, request):
        return Response({"message": "이메일, 비밀번호를 입력해주세요."})

    def post(self, request):

        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({f"message": "로그인 성공!"}, status=HTTP_200_OK)
        else:
            return Response(
                {"message": "이메일, 비밀번호를 확인해주세요."}, status=HTTP_400_BAD_REQUEST
            )


# 케이크 주인 로그아웃
class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({"message": "로그아웃 되었습니다."}, status=HTTP_200_OK)
