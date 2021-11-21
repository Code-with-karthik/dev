from rest_framework import serializers
from rest_framework.settings import api_settings
from django.contrib.auth import authenticate
from users.models import Customer
from django.utils.translation import ugettext_lazy as _
from rest_framework.validators import UniqueValidator


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

class LoginSerializer(serializers.Serializer):

    user_email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=Customer.objects.all())]
            )

    password = serializers.CharField(min_length=8)

    def create(self, validated_data):
        user = Customer.objects.create_user(validated_data['user_email'],
             validated_data['password'])
        return user

    class Meta:
        model = Customer
        fields = ('user_email', 'password')


