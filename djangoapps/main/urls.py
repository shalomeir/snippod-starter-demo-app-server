from django.conf.urls import include, url

from .views import IndexView, WebMasterView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    #for google webmaster
    url(r'google4c82de08f55a8973.html', WebMasterView.as_view(), name='googleWebMaster'),
]