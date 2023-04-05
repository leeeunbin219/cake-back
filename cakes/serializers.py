from rest_framework.serializers import ModelSerializer, SerializerMethodField,PrimaryKeyRelatedField
from .models import CakeBase, DecoCake

from users.serializers import UserSerializer


# 생일자 케이크 생성시 필요한 정보
class CreateCakeSerializer(ModelSerializer):
    class Meta:
        model = CakeBase
        fields = (
            "id",
            "nickname",
            "cakeshape",
            "cakecolor",
            "cream",
            "creamcolor",
            "image",
            "lettering",
        )


# 생일자가 케이크 조회 생성 수정 삭제시 필요한 정보
class CakeBaseSerializer(ModelSerializer):
    class Meta:
        model = CakeBase
        fields = (
            # "id",
            "email",
            "nickname",
            "cakeshape",
            "cakecolor",
            "cream",
            "creamcolor",
            "image",
            "lettering",
        )


# 방문자가 꾸민 케이크의 토핑 및 편지
class DecoCakeSerializer(ModelSerializer):
    usercake = PrimaryKeyRelatedField(queryset=CakeBase.objects.all())

    class Meta:
        model = DecoCake
        fields = "__all__"


# 방문자가 꾸민 케이크의 토핑 및 편지 수정 삭제
class DecoCakeDetailSerializer(ModelSerializer):

    # id = DecoCakeSerializer(read_only=True)
    usercake = CakeBaseSerializer(read_only=True)
    visitor_name = DecoCakeSerializer(read_only=True)
    visitor_password = DecoCakeSerializer(read_only=True)

    class Meta:
        model = DecoCake
        fields = ("usercake", "toppings", "letter", "visitor_name", "visitor_password")
