from django.db import models

# Create your models here.
class AdLocation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.name

class AdSpend(models.Model):
    location = models.ForeignKey(AdLocation, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.location.name} - {self.amount}"

class BusinessCrypto(models.Model):
    location = models.ForeignKey(AdLocation, on_delete=models.CASCADE)
    crypto_amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.location.name} - {self.crypto_amount}"
