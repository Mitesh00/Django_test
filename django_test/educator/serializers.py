from rest_framework import serializers
from educator.models import Educator

class EducatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educator
        fields = "__all__"
