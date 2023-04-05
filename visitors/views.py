from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Visitor
from .serializers import VisitorSerializer

from cake.models import UserCake, DecoCake
from cake.serializers import UserCakeSerializer, DecoCakeSerializer,MakeCakeSerializer


class VisitorView(APIView):
    
    def get(self, request):
        return Response({"message": "닉네임, 비밀번호를 입력해주세요."})
    
    def post(self, request):
        nickname = request.data.get("nickname")
        password = request.data.get("password")
        
        
        if not nickname:
            return Response({"message": "닉네임을 입력하세요."}, status=HTTP_400_BAD_REQUEST)
        if not password:
            return Response({"message": "비밀번호를 입력하세요."}, status=HTTP_400_BAD_REQUEST)
        
        cake = UserCake.objects.get(nickname=nickname)
        serializer = UserCakeSerializer(cake, data=request.data)
        if serializer.is_valid():
            visitor = serializer.save()
            visitor.set_password(password)
            visitor.save()
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

