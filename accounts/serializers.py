from rest_framework import serializers
from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, style={"input_type":"password"})
    password2 = serializers.CharField(write_only=True, style={"input_type":"password"})

    class Meta:
        model = Profile
        fields = ['id','username','password','password2']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Пароли не совпадають!')
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = Profile.objects.create_user(**validated_data)
        return user