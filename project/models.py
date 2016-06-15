from django.db import models

class Project(models.Model):
    menage = models.ForeignKey('auth.User')
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name
