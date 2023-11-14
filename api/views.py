
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializers
from tasks.models import Task, TaskImage
from rest_framework.permissions import IsAuthenticated


class TaskAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk=None, format=None):
        if pk is not None:
            # Retrieve a specific task by ID
            task = Task.objects.get(id=pk)
            serializer = TaskSerializers(task, many=False)
            return Response(serializer.data)
        else:
            # Retrieve all tasks for the authenticated user
            tasks = Task.objects.filter(user=request.user)
            serializer = TaskSerializers(tasks, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Ensure user is authenticated

        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            # Assign the authenticated user to the task
            task = serializer.save(user=request.user)

            # Handle images (if needed)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None, format=None):
        id = pk
        task = Task.objects.get(id=id)
        serializer = TaskSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Handle images (similar to the post method)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, delete=None):
        id = pk
        task = Task.objects.get(id=id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
