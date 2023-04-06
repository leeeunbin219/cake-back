from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    PrimaryKeyRelatedField,
)
from .models import CakeBase, DecoCake

from users.serializers import UserSerializer, MiniUserSerializer, VisitorSerializer


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


# 생일자가 케이크 조회 수정 삭제시 필요한 정보
class CakeDetailSerializer(ModelSerializer):
    user = MiniUserSerializer(read_only=True)

    class Meta:
        model = CakeBase
        fields = (
            "id",
            "user",
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
    usercake = MiniUserSerializer(read_only=True)

    class Meta:
        model = DecoCake
        fields = (
            "usercake_id",
            "usercake",
            "toppings",
            "letter",
            "visitor_name",
            "visitor_password",
        )
        read_only_fields = ("usercake",)
        # exclude = ("visitors_password",)


# 방문자가 꾸민 케이크의 토핑 및 편지 수정 삭제
class DecoCakeDetailSerializer(ModelSerializer):
    usercake = CakeDetailSerializer(read_only=True)

    class Meta:
        model = DecoCake
        fields = ("usercake", "toppings", "letter", "visitor_name","visitor_password")
        read_only_fields = ("id", "usercake")
