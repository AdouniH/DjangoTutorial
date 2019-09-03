from django.db import models

class Visitor(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    information = models.TextField()

    def __str__(self):
        return self.name


class RendezVous(models.Model):
    rdv_types = [('phone', 'phone'), ('sur_place', 'sur_place')]
    rdv_type = models.CharField(max_length=100, choices=rdv_types, blank=True)

    id = models.AutoField(primary_key=True)
    time = models.DateTimeField()

    def __str__(self):
        return self.time.strftime('%Y%m%d#%H:%M')

class token_rdv(models.Model):
    handeler_name = models.CharField(max_length=200)
    handeler_email = models.EmailField(max_length=254)
    input_text = models.TextField()
