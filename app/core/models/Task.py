from django.db import models


class Task(models.Model):
    '''Model for a task.'''
    PRIORITY_CHOICES = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low'),
    ]

    title = models.CharField(max_length=255, null=False)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES, default='L')
    due_date = models.DateField(null=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''Meta class for Task model.'''
        ordering = ['priority', 'due_date']

    def __str__(self):
        '''Return string representation of task.'''
        return self.title