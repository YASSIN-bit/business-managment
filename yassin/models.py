from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    
    def __str__(selfie):
        return f'{selfie.name} - {selfie.price}'
    # image_url = models.ImageField(max_length=2083)
    

class Identity(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    nationality = models.CharField(max_length=15)