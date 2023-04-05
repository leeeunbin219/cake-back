from rest_framework.views import APIView
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.exceptions import (
    NotFound,
    NotAuthenticated,
    ParseError,
    PermissionDenied,
)

from django.db import transaction

from .serializers import (
    CakeBaseSerializer,
    DecoCakeSerializer,
    DecoCakeDetailSerializer,
    CreateCakeSerializer,
)
from .models import CakeBase, DecoCake
from users.models import User


# 유저가 만든 케이크 생성
class UserCreateCake(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_cakes = CakeBase.objects.all()
        serializer = CreateCakeSerializer(
            all_cakes,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = CreateCakeSerializer(data=request.data)
        if serializer.is_valid():
            cake = serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# 유저가 만든 케이크 조회, 생성, 수정 및 삭제
class CakeBaseDetailViews(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return CakeBase.objects.get(pk=pk)
        except CakeBase.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        cake = self.get_object(pk)
        serializer = CakeBaseSerializer(cake)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        cake = self.get_object(pk)
        serializer = CakeBaseSerializer(
            cake,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_cake = serializer.save()
            return Response(CakeBaseSerializer(updated_cake).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cake = self.get_object(pk)
        cake.delete()
        return Response(status=HTTP_204_NO_CONTENT)


# 방문자가 꾸민 케이크의 토핑 및 편지
class DecoCakeViews(APIView):
    def get_object(self, pk):
        try:
            return CakeBase.objects.get(pk=pk)
        except CakeBase.DoesNotExist:
            return NotFound(status=HTTP_400_BAD_REQUEST)
        
    def get(self,request,pk):
        cake = self.get_object(pk)
        serializer = DecoCakeSerializer(cake)
        return Response(serializer.data, status=HTTP_200_OK)
    

    def post(self, request, pk):
        serializer = DecoCakeSerializer(data=request.data)
        if serializer.is_valid():
            decocake = serializer.save(
                nickname=request.data.get("nickname"),
                usercake=self.get_object(pk=pk),
            )
            serializer = DecoCakeSerializer(decocake)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# 방문자가 꾸민 케이크의 토핑 및 편지 조회 수정 삭제
# 방문자는 조회/수정/삭제 가능 // 유저는 삭제만 가능
class DecoDetailView(APIView):
    def get_object(self, pk):
        try:
            return DecoCake.objects.get(pk=pk)
        except DecoCake.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        decocake = self.get_object(pk)
        if decocake.visitor_name != request.data.get("visitor_name"):
            raise PermissionDenied()
        serializer = DecoCakeDetailSerializer(decocake)
        return Response(serializer.data, status=HTTP_200_OK)

    def put(self, request, pk):
        decocake = self.get_object(pk)

        if decocake.visitor_name != request.data.get("visitor_name"):
            raise PermissionDenied()

        serializer = DecoCakeDetailSerializer(
            decocake,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_decocake = serializer.save()
            return Response(DecoCakeDetailSerializer(updated_decocake).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        decocake = self.get_object(pk)
        
        if not request.user.is_authenticated:
            raise PermissionDenied()
        
        user_email = request.data.get("user_email")
        visitor_name = request.data.get("visitor_name")
        visitor_password = request.data.get("visitor_password")
        
        if decocake.usercake.email != user_email or decocake.visitor_name != visitor_name:
            raise PermissionDenied()
        
        if not decocake.visitor_password == visitor_password:
            raise PermissionDenied()
        
        decocake.delete()
        
        return Response(status=HTTP_204_NO_CONTENT)