from django.urls import re_path
from .views import Index, Api

app_name = 'app'
urlpatterns = [
    re_path(r'^$', Index.as_view(), name="index"),
    re_path(r'^api/$', Api.as_view(), name="api"),
]
