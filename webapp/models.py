from django.db import models

status_choices = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]

class Task(models.Model):
    description = models.CharField(max_length=500)
    details = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choices, default='new')
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.description
