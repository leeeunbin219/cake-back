import re
from rest_framework.exceptions import ParseError, ValidationError
from rest_framework.serializers import ModelSerializer
from .models import User
# from visitors.models import Visitor

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




# 로그인 시 필요한 정보
class UserLoginSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "email",
            "password",
        )
        
