from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.authtoken.models import Token


class SignupSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=150)

    def get_password_serializer(self):
        return serializers.CharField(max_length=128)

    def __init__(self, with_password=True, *args, **kwargs):
        super(SignupSerializer, self).__init__(*args, **kwargs)

        if with_password:
            self.fields['password'] = self.get_password_serializer()


class LoginSerializer(serializers.Serializer):
    username = serializers.EmailField(max_length=255)
    password = serializers.CharField(max_length=128)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'is_active', 'last_name')


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    msg = _('Sorry, this account is currently inactive.contact to administrator.')
                    raise exceptions.ValidationError(msg)
            else:
                msg = _('There was a problem with your email and password combination. Please try again.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Must include "username" and "password".')
            raise exceptions.ValidationError(msg)

        data = dict()
        data['user'] = UserSerializer(user).data
        token, created = Token.objects.get_or_create(user=user)
        data['token'] = token.key

        return data
