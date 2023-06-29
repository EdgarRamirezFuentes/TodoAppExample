from rest_framework import serializers

from core.models import Task

class TaskSerializer(serializers.ModelSerializer):
    '''Serializer for Task model.'''
    class Meta:
        model = Task
        fields = '__all__'

    def validate_title(self, title):
        '''Validate title.'''
        if not title:
            raise serializers.ValidationError('Title is required.')
        return title
    
class SimpleTaskSerializer(serializers.ModelSerializer):
    '''Serializer for Task model.'''
    class Meta:
        model = Task
        fields = ['id', 'title', 'priority', 'due_date', 'completed']

    