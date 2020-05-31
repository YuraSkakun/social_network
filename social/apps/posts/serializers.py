from rest_framework import serializers
from .models import Post, UserLike


class UserLikeBriefSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLike
        fields = ('id', 'user', 'active')


class PostSerializer(serializers.ModelSerializer):

    likes = UserLikeBriefSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'date', 'user', 'likes')


class UserLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLike
        fields = ('id', 'user', 'post', 'active', 'date', 'update')
