import logging

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Post, Comment
from .serializers import CommentSerializer, PostSerializer

logger = logging.getLogger(__name__)


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(methods=['post'], detail=True, url_path='up-vote')
    def up_vote(self, request, pk=None):
        post = get_object_or_404(Post, id=pk)
        post.up_votes_amount += 1
        post.save()
        return Response('Created', status=201)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        queryset = Comment.objects.all()

        post_id = self.request.query_params.get('post_id', None)

        if post_id is not None:
            queryset = queryset.filter(post__id=post_id)
        return queryset

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.request.data.get('post_id'))
        return serializer.save(post=post)
