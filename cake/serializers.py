from rest_framework import serializers
from .models import UserCake, DecoCake
from users.serializers import SignupSerializer
from visitors.serializers import VisitorSerializer

class UserCakeSerializer(serializers.ModelSerializer):
    
    letters = VisitorSerializer(many=True, read_only=True)
    # visitor = VisitorSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserCake
        fields = "__all__"
        

class DecoCakeSerializer(serializers.ModelSerializer):
    
    usercake = UserCakeSerializer(many=True, read_only=True)
    
    class Meta:
        model = DecoCake
        fields = "__all__"
        
        

class MakeCakeSerializer(serializers.ModelSerializer):
    
    usercake = UserCakeSerializer(many=True, read_only=True)
    visitor = VisitorSerializer(many=True, read_only=True)
    
    class Meta:
        model = UserCake, DecoCake
        fields = "__all__"