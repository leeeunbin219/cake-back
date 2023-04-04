from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_201_CREATED, HTTP_204_NO_CONTENT,HTTP_400_BAD_REQUEST
from .models import UserCake, DecoCake
from .serializers import UserCakeSerializer, DecoCakeSerializer



class UserCakes(APIView):
    
    def get(self, request):
        cakes = UserCake.objects.filter(user=request.user)
        serializer = UserCakeSerializer(cakes, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        cake = UserCake.objects.get(id=id)
        serializer = UserCakeSerializer(data=request.data)
        if not request.user:
            return Response({"message": "로그인이 필요합니다."}, status=HTTP_400_BAD_REQUEST)
        else:
            if serializer.is_valid():
                cake = request.data.get("usercake")
                if not cake:
                    return Response({"message": "케이크를 선택하세요."}, status=HTTP_400_BAD_REQUEST)
                else:
                    return Response(serializer.data, status=HTTP_201_CREATED)

    def delete(self, request):
        cake = UserCake.objects.get(id=id)
        cake.delete()
        return Response(status=HTTP_204_NO_CONTENT)