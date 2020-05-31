from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import UserSerializer, GroupSerializer, UserActivitySerializer

from rest_framework.permissions import IsAdminUser


@api_view(['GET'])
def api_root(request, format=None):
    """
    The entry endpoint of our API.
    """
    return Response({
        'users': reverse('user-list', request=request),
        'groups': reverse('group-list', request=request),
        'rest_registration': reverse('rest_registration:register', request=request),
        'rest_framework_login': reverse('rest_framework:login', request=request),
        'user_profile': reverse('user_profile_list', request=request),
        'posts': reverse('post_list', request=request),
        'user_like_list_by_day': reverse('user_like_list_by_day', request=request),
    })


class UserList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of users.
    """
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single user.
    """
    model = User
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get('pk'))


class GroupList(generics.ListCreateAPIView):
    """
    API endpoint that represents a list of groups.
    """
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser]


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represents a single group.
    """
    model = Group
    serializer_class = GroupSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        return get_object_or_404(Group, pk=self.kwargs.get('pk'))


class UserActivityDetail(generics.RetrieveAPIView):
    """
    API endpoint that represents a  user activity.
    """
    model = User
    serializer_class = UserActivitySerializer
    # permission_classes = [IsAdminUser]

    def get_object(self):
        user =  get_object_or_404(User, pk=self.kwargs.get('pk'))
        print(user.last_login)
        return user
