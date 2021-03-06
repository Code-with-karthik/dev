from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

#URLConf
urlpatterns = [
    path('', views.index),
    path('home/', views.home),
    path('hello/', views.HelloView.as_view(), name='hello')
]

urlpatterns = format_suffix_patterns(urlpatterns)
