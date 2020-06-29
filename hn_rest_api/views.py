from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_queryset(self):
        queryset = Comment.objects.all()

        post_id = self.request.query_params.get('post_id', None)

        if post_id is not None:
            queryset = queryset.filter(post__id=post_id)
        return queryset
