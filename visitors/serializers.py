from rest_framework import serializers
from .models import Visitor


class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        exclude = (
            # "password",
            "created_at",
            "updated_at",
        )
