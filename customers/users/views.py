from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User, Group
from users.models import Customer
from users.serializers import UserSerializer
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext, context


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

"""
class GroupViewSet(viewsets.ModelViewSet):
    ""
    API endpoint that allows groups to be viewed or edited.
    ""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
"""

def login_user(request):
    logout(request)
    username = password = ''
    info = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        info = {'user': username}
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                request.session['user'] = username
                info['user'] = username
                return HttpResponseRedirect('/usersinfo/home/', info)
    return render(request, 'login.html')

@login_required(login_url='/usersinfo/login/')
def home(request):
     return render(request, 'helloworld.html', {'Name' : request.session.get('user')})