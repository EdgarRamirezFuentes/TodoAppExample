from core.models import Task
from .serializers import TaskSerializer, SimpleTaskSerializer
from rest_framework import viewsets, response

import datetime

class TaskViewSet(viewsets.ModelViewSet):
    '''ViewSet for Task model.'''
    authentication_classes = []
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def retrieve(self, request, *args, **kwargs):
        '''Retrieve a task by Id.'''
        instance = self.get_object()
        serializer = SimpleTaskSerializer(instance)
        return response.Response(serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        '''Update a task.'''

        # Set the completed_date if the task is being marked as completed.
        is_completed = request.data.get('completed', False)

        if is_completed:
            now = datetime.date.today()
            request.data['completed_date'] = datetime.date.isoformat(now)
            print(request.data['completed_date'])
        else:
            request.data['completed_date'] = None

        return super().partial_update(request, *args, **kwargs)