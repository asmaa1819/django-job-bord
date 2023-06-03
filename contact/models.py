from django.db import models

class Info(models.Model):
    place=models.CharField( max_length=50)
    phone=models.CharField( max_length=20)
    email=models.EmailField( max_length=254)


    def __str__(self):
        return self.email

    

