from django.shortcuts import render, redirect
import json
from rest_framework import viewsets, parsers
from rest_framework.views import APIView, Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User, Group
from users.models import Customer
from users.serializers import UserSerializer
from django.http import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template import RequestContext, context
from django.core.exceptions import ValidationError

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
def index(request):
    return JsonResponse({'info':'A Simple Custom User Page', 'developer':'Karthik'})

@api_view(["POST"])
@permission_classes([AllowAny])
def login_user(request):
    logout(request)
    username = r_password = ''
    info = {}
    reqBody = json.loads(request.body)
    email1 = reqBody['user_email']
    r_password = reqBody['password']
    #print(email1, password)
    try:
        Account = Customer.objects.get(user_email = email1)
        print(Account.user_email, Account.password)
    except BaseException as e:
            raise ValidationError({"400": f'{str(e)}'})
    
    token = Token.objects.get_or_create(user=Account)[0].key
    #print(token)
    if Account:
            if Account.is_active:
                print(request.user)
                login(request, Account)
                info["message"] = "user logged in"
                info["email_address"] = Account.user_email
                Res = {"data": info, "token": token}
                
                if not Customer.check_password(Account, r_password):
                    raise ValidationError({"message": "Incorrect Login credentials"})

                return Response(Res)

            else:
                raise ValidationError({"400": f'Account not active'})
    else:
        raise ValidationError({"400": f'Account doesnt exist'})

    """
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
                return HttpResponseRedirect('/home/', info)
    return render(request, 'login.html')
    """

@login_required(login_url='/login/')
def home(request):
     return render(request, 'helloworld.html', {'Name' : request.session.get('user')})