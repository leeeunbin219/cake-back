from rest_framework.serializers import ModelSerializer
from .models import User
# from visitors.models import Visitor


class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = (
            # "pk",
            "name",
            "nickname",
            "email",
            "password",
            "birthday",
            # "visitor",
        )

