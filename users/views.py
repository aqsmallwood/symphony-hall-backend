from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from django.contrib.auth.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def create(self, request):
        form = UserCreationForm(request.data)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            return Response({'success': True}, status=201)

        return Response({'success': 'False'}, status=400)
