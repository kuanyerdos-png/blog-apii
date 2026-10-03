from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from .views import (
    CategoryViewSet,
    CommentViewSet,
    PostViewSet,
    TagViewSet,
)

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"tags", TagViewSet)
router.register(r"posts", PostViewSet)

posts_router = routers.NestedDefaultRouter(
    router,
    r"posts",
    lookup="post",
)
posts_router.register(
    r"comments",
    CommentViewSet,
    basename="post-comments",
)

urlpatterns = [
    path("", include(router.urls)),
    path("", include(posts_router.urls)),
]
