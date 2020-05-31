from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from .models import Post, UserLike
from .serializers import PostSerializer, UserLikeSerializer
from .permissions import IsOwner


# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_object(self):
        obj = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return obj


class UserLikeList(generics.ListCreateAPIView):
    serializer_class = UserLikeSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = UserLike.objects.all()
        request = self.request

        if request.GET.get('date_from') and request.GET.get('date_to'):
            date_from = request.GET.get('date_from')
            date_to = request.GET.get('date_to')

            queryset = UserLike.objects.filter(
                date__range=(date_from, date_to)).order_by('-date')

            # queryset = UserLike.objects.filter(
            #     date__gte=date_from, date__lte=date_to).order_by('-date')

        return queryset


class UserLikeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserLikeSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def get_object(self):
        obj = get_object_or_404(UserLike, pk=self.kwargs.get('user_like_id'))#, user=self.request.user)
        return obj


class UserLikeListByDay(generics.ListCreateAPIView):
    serializer_class = UserLikeSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = UserLike.objects.all()
        request = self.request

        if request.GET.get('date_from') and request.GET.get('date_to'):
            date_from = request.GET.get('date_from')
            date_to = request.GET.get('date_to')

            queryset = UserLike.objects.filter(
                date__range=(date_from, date_to)).order_by('-date')

        return queryset.order_by('-date')
