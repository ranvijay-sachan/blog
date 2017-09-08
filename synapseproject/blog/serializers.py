from rest_framework import serializers
from .models import Post, Comment


class PostsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('id', 'title', 'owner', 'text', 'post_date')


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Comment
        fields = ('id', 'post', 'owner', 'text', 'comment_date')


class FlagSerializer(serializers.Serializer):
    """
    Contains a true/false flag state
    """
    state = serializers.BooleanField(required=True)