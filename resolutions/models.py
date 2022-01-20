from django.db import models

class Resolution(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    done = models.BooleanField()
    category = models.ForeignKey('ResolutionCategory', on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class ResolutionCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
