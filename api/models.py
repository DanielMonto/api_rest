from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.TextField()
    description=models.TextField(blank=True,null=True)
    completed=models.BooleanField(default=False)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.name)
    class Meta:
        ordering=['-updated']