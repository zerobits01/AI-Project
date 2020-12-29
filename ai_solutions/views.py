from rest_framework.views import APIView
from rest_framework.response import Response 
from django.http import JsonResponse


class SayHello(APIView):
    """this is a test for the api view"""
    
    def get(self, request, format=None):
        """this gonna return a hello worl message and an array"""
        data = [
            'get, post, patch, put, delete',
            'and this is a test',
        ]
        return Response({'message': "hello-world! from rest api!", 'an_apiview' : data})


class Solver(APIView):
    """this is the ai maze solver that connects to the channels, web socket"""

    def get(self, request, method, format=None):
        """this just return the name of the algorithm they try to use"""
        return Response({
            'message': "this is an optional message",
            'method' : f"{method}",
        })


def testChannel(request, method):

    return JsonResponse({
            'message': "this is an optional message",
            'method' : f"{method}",
    })
