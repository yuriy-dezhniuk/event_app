from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.TextField(max_length=300)
    location = models.TextField(max_length=250)
    image = models.ImageField(upload_to='events')
    description = models.TextField()
    event_data = models.DateField()

    def __str__(self):
        return f'{ self.title }'

