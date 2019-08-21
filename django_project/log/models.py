from django.db import models

class Visitor(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    information = models.TextField()

    def __str__(self):
        return self.name