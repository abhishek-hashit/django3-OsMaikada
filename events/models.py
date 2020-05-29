from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title