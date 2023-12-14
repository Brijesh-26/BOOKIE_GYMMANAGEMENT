from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Gym, Trainer, Client, WorkoutSession
from .serializers import GymSerializer, TrainerSerializer, ClientSerializer, WorkoutSessionSerializer
from django.http import Http404
from .permissions import IsTrainerForWorkoutSession
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Gyms

@api_view(['GET', 'POST'])
def gym_list(request):
    if request.method == 'GET':
        gyms = Gym.objects.all()
        serializer = GymSerializer(gyms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GymSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def gym_detail(request, pk):
    try:
        gym = Gym.objects.get(pk=pk)
    except Gym.DoesNotExist:
        return Response({"error": "Gym not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GymSerializer(gym)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GymSerializer(gym, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        gym.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Trainers

@api_view(['GET', 'POST'])
def trainer_list(request):
    if request.method == 'GET':
        trainers = Trainer.objects.all()
        serializer = TrainerSerializer(trainers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TrainerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def trainer_detail(request, pk):
    try:
        trainer = Trainer.objects.get(pk=pk)
    except Trainer.DoesNotExist:
        return Response({"error": "Trainer not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TrainerSerializer(trainer)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TrainerSerializer(trainer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        trainer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Clients

@api_view(['GET', 'POST'])
def client_list(request):
    if request.method == 'GET':
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Workout Sessions


@api_view(['GET', 'POST'])
def workout_session_list(request):
    if request.method == 'GET':
        sessions = WorkoutSession.objects.all()
        serializer = WorkoutSessionSerializer(sessions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = WorkoutSessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsTrainerForWorkoutSession])
def workout_session_detail(request, pk):
    try:
        session = WorkoutSession.objects.get(pk=pk)
    except WorkoutSession.DoesNotExist:
        return Response({"error": "Workout Session not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = WorkoutSessionSerializer(session)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = WorkoutSessionSerializer(session, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        session.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)