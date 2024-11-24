from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, TicketSerializer
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Ticket
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import Is_Super_Stuff_Owner, Is_Super__Owner


class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketCreateView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, rq, *args, **kwargs):
        ser = TicketSerializer(data=rq.data)
        if ser.is_valid():
            print("-" * 100)
            print(rq.user)
            print("-" * 100)
            ser.save(user=rq.user)
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)


class TicketSingleView(generics.RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, Is_Super_Stuff_Owner]


class TicketDelandUpdate(generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, Is_Super__Owner]

    def put(self, request, *args, **kwargs):
        return self.update(request, partial=True)


class UserView(APIView):
    def post(self, rq):
        user_ser = UserSerializer(data=rq.data)
        if user_ser.is_valid():
            user_ser.save()
            # print("*"*124)
            # print(rq.user)
            # print("*"*124)
            return Response({"msg": "User created successfully"}, status=201)
        else:
            return Response(user_ser.errors, status=400)
