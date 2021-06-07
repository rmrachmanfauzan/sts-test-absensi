from django.db import models

class Absen(models.Model):
    user = models.ForeignKey("User", verbose_name=("user"), on_delete=models.CASCADE)
    tanggal = models.DateTimeField(auto_now=False, auto_now_add=False)
    absen_in = models.DateTimeField(blank=True,null=True, auto_now=False, auto_now_add=False)
    absen_out = models.DateTimeField(blank=True,null=True, auto_now=False, auto_now_add=False)