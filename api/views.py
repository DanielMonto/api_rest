from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
# Create your views here.
@api_view(['GET'])
def main_drf(request):
    route=[
        {
            "hello":"world"
        }
    ]
    return Response(route)
class TaskListView(generics.ListAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
class TaskCreateView(generics.CreateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
class TaskDeleteView(generics.DestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
class TaskPutView(generics.UpdateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
class GetTaskView(generics.RetrieveAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer