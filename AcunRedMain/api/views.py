from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.

class LoginViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer

    def login(self, request):
        # Get the username and password from the request
        username = request.data['username']
        password = request.data['password']

        # Authenticate the user
        user = authenticate(username=username, password=password)

        # If the user is authenticated, return a success response
        if user is not None:
            return Response({'success': True, 'user': user.username})

        # If the user is not authenticated, return a failure response
        else:
            return Response({'success': False, 'error': 'Invalid username or password'})
