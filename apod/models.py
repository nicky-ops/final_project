from django.db import models

# Create your models here.
class Apod(models.Model):
    date = models.DateField(unique=True)
    title = models.CharField(max_length=200)
    explanation = models.TextField()
    url = models.URLField()
    media_type = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f"{self.date}: {self.title}"
