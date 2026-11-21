from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Registration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.name