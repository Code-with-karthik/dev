from django.contrib.auth.models import User, Group
from rest_framework import serializers
from users.models import Customer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['url', 'user_name', 'user_email', 'password', 'first_name', 'last_name']

"""
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
"""