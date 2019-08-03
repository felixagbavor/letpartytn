from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response



def index(request):
    return render(request,'partytn/index.html',{})


# API for Party Data from DB
class PartyData(APIView):
    
    authentication_classes = []
    permission_classes =[]

    def get(self, request, format=None):
        
        data = {
            "numOfParties": 10,

        }


        return Response(data)


