from rest_framework import serializers
from .models import *


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class courseserializer(serializers.ModelSerializer):
    class Meta:
        model = course
        fields = '__all__'
class studentserializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'