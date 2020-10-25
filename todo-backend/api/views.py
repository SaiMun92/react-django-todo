from django.shortcuts import render
from .serializers import TodoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Todo


# Create your views here.
@api_view(['GET'])
def taskList(request):
    tasks = Todo.objects.all().order_by('-id')
    serializer = TodoSerializer(tasks, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Todo.objects.get(id=pk)
    serializer = TodoSerializer(tasks, many=False)
    return Response(data=serializer.data)


@api_view(['POST'])
def taskCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def taskUpdate(request, pk):
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializer(instance=task, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Todo.objects.get(id=pk)
    task.delete()

    return Response(status=status.HTTP_200_OK)
