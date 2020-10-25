from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    identify_code = models.CharField(max_length=500)
    password_sha256 = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=50)
    identify_code = models.CharField(max_length=500)
    password_sha256 = models.CharField(max_length=256)
    def __str__(self):
        return self.name

class Bill(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    money = models.FloatField()
    start_date = models.DateTimeField()
    during_time = models.TimeField()
    client_certificate = models.CharField(max_length=256, default=None)
    expiration = models.DateTimeField(default=None)
    status = models.IntegerField(default=0)
    ensure_time = models.DateTimeField(default=None)
    def __str__(self):
        return self.bank.name + " => " + self.client.name