from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, FollowingViewSet, CommentViewSet

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register('follow', FollowingViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>\d+)/comments/',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('auth/', include('djoser.urls.jwt')),
]
