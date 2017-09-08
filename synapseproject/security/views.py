# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from serializers import (SignupSerializer,
                         LoginSerializer,
                         AuthTokenSerializer, UserSerializer)


class Logout(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """Remove all auth tokens owned by request.user"""
        tokens = Token.objects.filter(user=request.user)
        for token in tokens:
            token.delete()
        content = {'sucess': 'User logged out.'}
        return Response(content, status=status.HTTP_200_OK)


class Signup(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                User.objects.get(email=request.data['email'])
                content = {'detail': 'User with this Email address already exists.'}
                return Response(content, status=status.HTTP_409_CONFLICT)
            except User.DoesNotExist:
                user_data = serializer.data
                user_data['is_active'] = True
                user_data['last_login'] = timezone.now()
                user = User.objects.create(**user_data)
                if 'password' in serializer.data:
                    user.set_password(serializer.data['password'])
                user.save()
                content = {'detail': 'Your registration done succesfully.'}
                return Response(content, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Login(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def post(self, request, format=None):
        try:
            data = request.data
            serializer = AuthTokenSerializer(data=data, context={'request': request})
            if serializer.is_valid():
                return Response(serializer.validated_data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except BaseException as e:
            return Response(e.message, status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

