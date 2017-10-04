from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class EventDate(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.event, str(self.pub_date)
