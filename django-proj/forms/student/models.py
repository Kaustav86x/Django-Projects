from email.policy import default
from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

class Student(models.Model):
    name = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Name must be greater than 2 characters")]
    )
    roll = models.CharField(max_length=10, default="")
    email = models.CharField(max_length=128, default="")
    password = models.CharField(max_length=200, default = "")

    # returning the object (in string format)
    # it is supposed to return a string type data 
    def __str__(self):
        return ("Name = "+ self.name + ",  Roll.: = " + self.roll + ",  Email = " + self.email)

