from django.db import models

# Create your models here.
class Mail(models.Model):
	recipient = models.CharField(max_length=50)
	subject = models.CharField(max_length=50)
	body = models.CharField(max_length=255)


class Ocr(models.Model):
	nip = models.CharField(max_length=10)
	regon = models.CharField(max_length=15)
	krs = models.CharField(max_length=15)
	name = models.CharField(max_length=150)

class Check(models.Model):
	nip = models.CharField(max_length=10)

class Compare(models.Model):
	nip1 = models.CharField(max_length=10)
	regon1 = models.CharField(max_length=15)
	krs1 = models.CharField(max_length=15)
	name1 = models.CharField(max_length=150)
	nip2 = models.CharField(max_length=10)
	regon2 = models.CharField(max_length=15)
	krs2 = models.CharField(max_length=15)
	name2 = models.CharField(max_length=150)

class Tag(models.Model):
	billtoname = models.CharField(max_length=100)
	billtovat = models.CharField(max_length=100)
	created = models.CharField(max_length=30)
	number = models.CharField(max_length=100)
	total = models.CharField(max_length=100)

class Tax(models.Model):
	description1 = models.CharField(max_length=100)
	price1 = models.CharField(max_length=100)
	total1 = models.CharField(max_length=30)
	description2 = models.CharField(max_length=100)
	price2 = models.CharField(max_length=100)
	total2 = models.CharField(max_length=100)

class Danek(models.Model):
	nip = models.CharField(max_length=10)
	name = models.CharField(max_length=150)

