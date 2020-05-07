from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.exceptions import ValidationError


User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(label='Password', min_length=4, write_only=True,
                                     style={'input_type': 'password', 'placeholder': 'Password'})
    password2 = serializers.CharField(label='Confirm Password', min_length=4, write_only=True,
                                     style={'input_type': 'password', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ('role', 'username', 'password', 'password2',)

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        role = validated_data['role']
        user = User(username=username, password=password, role=role)

        if password != validated_data['password2']:
            raise ValidationError('Passwords not match!')
        else:
            user.set_password(password)
            user.save()
        return validated_data



