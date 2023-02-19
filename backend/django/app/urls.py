from django.conf.urls import url
from .views import Index, Api

app_name = 'app'
urlpatterns = [
    url(r'^$', Index.as_view(), name="index"),
    url(r'^api/$', Api.as_view(), name="api"),
]
