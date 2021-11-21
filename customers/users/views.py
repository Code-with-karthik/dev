from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from users.models import Customer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

class HelloView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)

def index(request):
    return JsonResponse({'info':'A Simple Custom User Page', 'developer':'Karthik'})

@login_required(login_url='/login/')
def home(request):
     return render(request, 'helloworld.html', {'Name' : request.session.get('user')})

