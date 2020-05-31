from django.shortcuts import render, get_object_or_404

from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from apps.users.models import UserProfile, UserAddress, UserPhone
from apps.users.permissions import IsOwner
from apps.users.serializers import (
    UserProfileSerializer, UserAddressSerializer, UserPhoneSerializer
)


class UserProfileList(generics.ListCreateAPIView):
    serializer_class = UserProfileSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserProfile.objects.all() #filter(user=self.request.user)


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_object(self):
        return get_object_or_404(
            UserProfile,
            pk=self.kwargs.get('user_profile_id')
        )


class UserAddressList(generics.ListCreateAPIView):
    serializer_class = UserAddressSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return UserAddress.objects.all() #filter(user_profile__user=self.request.user)


class UserAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserAddressSerializer

    def get_object(self):
        return get_object_or_404(
            UserAddress,
            pk=self.kwargs.get('user_address_id')
        )


class UserPhoneList(generics.ListCreateAPIView):
    serializer_class = UserPhoneSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UserPhone.objects.all() #filter(user_profile__user=self.request.user)


class UserPhoneDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserPhoneSerializer

    def get_object(self):
        return get_object_or_404(
            UserPhone,
            pk=self.kwargs.get('user_phone_id')
        )
