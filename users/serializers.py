import re
from rest_framework.exceptions import ParseError, ValidationError
from rest_framework.serializers import ModelSerializer
from .models import User
from cakes.models import DecoCake

# 회원가입 시 필요한 정보
class SignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            # "pk",
            "name",
            "nickname",
            "email",
            "password",
            "birthday",
        )

    def validate_password(self, password):

        if password:
            if not re.search(r"[a-z,A-Z]", password):
                raise ValidationError("비밀번호는 영문을 포함해야 합니다.")
            if not re.search(r"[0-9]", password):
                raise ValidationError("비밀번호는 숫자를 포함해야 합니다.")
            if len(password) < 8 or len(password) > 16:
                raise ValidationError("비밀번호는 8자 이상 16자 이하이어야 합니다.")
            print(password)
        else:
            raise ParseError("비밀번호를 입력하세요.")
        return password


# 유저 정보 조회 및 수정 삭제 (user용)
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "name",
            "nickname",
            "email",
            "password",
            "birthday",
        )


# 유저 정보 간략히 조회 (view 사용)
class MiniUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "nickname",
            "email",
            "birthday",)


# 유저 정보 자세히 조회 (admin용)
class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "name",
            "nickname",
            "email",
            "birthday",
            "is_active",
            "is_admin",
            "date_joined",
            "last_login",
        )


# 로그인 시 필요한 정보
class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )


# visitor 정보
class VisitorSerializer(ModelSerializer):
    class Meta:
        model = DecoCake
        fields = (
            # "usercake",
            "visitor_name",
            # "visitor_password",
        )


