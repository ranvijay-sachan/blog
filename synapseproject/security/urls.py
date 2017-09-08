from django.conf.urls import url, include
from security import views as v
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', v.UserProfileViewSet)


# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'login/$', v.Login.as_view(), name="login"),
    url(r'logout/$', v.Logout.as_view(), name="logout"),
    url(r'signup/$', v.Signup.as_view(), name="signup"),
]

