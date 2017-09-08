from django.conf.urls import url, include
from blog import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'posts', views.PostsViewSet)
router.register(r'comment', views.CommentViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]
