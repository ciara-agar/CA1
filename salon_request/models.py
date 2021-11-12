from django.db import models
from django.urls import reverse
from django.db.models.deletion import CASCADE

# Create your models here.
class Request(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE
    )

    body = models.TextField()

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('request_detail', args=[str(self.id)])