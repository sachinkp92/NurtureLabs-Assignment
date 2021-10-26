from django.shortcuts import render, HttpResponse
from rest_framework import viewsets
from .serializers import AdvisorSerializer, UserSerializer, UserloginSerializer, AdvisorbookSerializer
from .models import Advisor, User, Advisorbook
from rest_framework import generics

# Create your views here.
def index(request):
    return HttpResponse('Hello World')


class AdvisorList(generics.ListCreateAPIView):
    queryset = Advisor.objects.all()
    serializer_class = AdvisorSerializer

class AdvisorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advisor
    serializer_class = AdvisorSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = UserSerializer

class UserloginList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserloginSerializer

class UserloginDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User
    serializer_class = UserloginSerializer


class AdvisorbookList(generics.ListCreateAPIView):
    queryset = Advisorbook.objects.all()
    serializer_class = AdvisorbookSerializer

class AdvisorbookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advisor
    serializer_class = AdvisorbookSerializer
