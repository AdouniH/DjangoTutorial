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
    token = models.BooleanField()

    def __str__(self):
        return self.time.strftime('%d/%m/%Y - %H:%M')

class Token_rdv(models.Model):
    CHOICES = [
        ("1", 'moins de 15min'),
        ("2", 'entre 15min et 30min'),
        ("3", 'plus que 30min')
    ]
    name = models.CharField(max_length=200, verbose_name="Votre nom")
    email = models.EmailField(max_length=254, verbose_name="Votre email")
    company = models.CharField(max_length=254, verbose_name="Nom de l'entreprise")
    duration = models.CharField(
        max_length=2,
        choices=CHOICES,
        default="1",
        verbose_name="durée de l'appel prévue"
    )
    commentaire = models.TextField()
    rdv_shift = models.ForeignKey(
        'RendezVous',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return "{} - {}".format(self.company, self.rdv_shift)
