from django.db import models

class Blog_project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    date = models.DateField()
    url = models.URLField(blank=True)


    def __str__(self):
        return self.title
