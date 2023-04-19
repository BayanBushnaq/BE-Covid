from django.shortcuts import render
from rest_framework.generics import  RetrieveUpdateDestroyAPIView ,ListCreateAPIView
from .serializers  import CovidSerializer
from .models import Covid



class MyRecords(ListCreateAPIView):
    queryset = Covid.objects.all()
    serializer_class= CovidSerializer
    

class CovidDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Covid.objects.all()
    serializer_class= CovidSerializer
# Create your views here.
