from django.db import models

# Create your models here.
class Mail(models.Model):
	recipient = models.CharField(max_length=50)
	subject = models.CharField(max_length=50)
	body = models.CharField(max_length=255)

<<<<<<< HEAD
class Ocr(models.Model):
	nip = models.CharField(max_length=10)
	regon = models.CharField(max_length=15)
	krs = models.CharField(max_length=15)
=======
class Check(models.Model):
	nip = models.CharField(max_length=10)
>>>>>>> 4a6afaeab0764dbb31e5a856eb52482b01ecbee0
