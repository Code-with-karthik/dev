from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.urlpatterns import format_suffix_patterns

#URLConf
urlpatterns = [
    path('login/', views.login_user),
    path('', views.index),
    path('home/', views.home),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
