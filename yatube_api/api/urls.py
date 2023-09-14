from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    PostViewSet,
    GroupViewSet,
    FollowingViewSet,
    CommentViewSet
)

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

follow_list = FollowingViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('v1/follow/', follow_list, name='follow-list'),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
