from django.conf.urls import include, url
from rest_framework import routers
from authentication.views import AccountViewSet, LoginView, LoadAuthView, LogoutView


router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'auth/login/', LoginView.as_view(), name='login'),
    url(r'auth/load_auth/', LoadAuthView.as_view(), name='load_auth'),
    url(r'auth/logout/', LogoutView.as_view(), name='logout')
]