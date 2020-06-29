from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet

app_name = "hn_rest_api"

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls
