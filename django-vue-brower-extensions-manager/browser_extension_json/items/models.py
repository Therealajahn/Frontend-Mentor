from django.db import models

class Item(models.Model):

    logo = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    description = models.TextField()
    isActive = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
