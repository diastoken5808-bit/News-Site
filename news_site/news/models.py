from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    image = models.URLField(null=True, blank=True)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title

class SearchQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    query = models.CharField(max_length=255)
    num = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.query}"