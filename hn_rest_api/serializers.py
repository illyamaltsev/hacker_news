from rest_framework import serializers
from .models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('author_name', 'content', 'creation_date', 'post_id')


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'link', 'author_name', 'up_votes_amount', 'creation_date')


class PostWithCommentsSerializer(PostSerializer):
    comments = CommentSerializer(many=True, read_only=True)