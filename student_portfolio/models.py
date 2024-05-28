from django.db import models


class Apps(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=118)
    url = models.CharField(max_length=118)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.title
