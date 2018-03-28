from django.db import models

class SomeOne(models.Model):
    email = models.CharField(max_length=200)

    password = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    birthdate = models.CharField(max_length=200)
    birthplace = models.CharField(max_length=200)
    address = models.CharField(max_length=800)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    zip = models.CharField(max_length=200)

    smartphone = models.BooleanField(default=False)
    laptop = models.BooleanField(default=False)
    tablet = models.BooleanField(default=False)

    Art = models.BooleanField(default=False)
    Auto = models.BooleanField(default=False)
    Beauty = models.BooleanField(default=False)
    Books = models.BooleanField(default=False)
    Business =  models.BooleanField(default=False)
    Communication = models.BooleanField(default=False)
    Dating = models.BooleanField(default=False)
    Education = models.BooleanField(default=False)
    Entertainment = models.BooleanField(default=False)
    Finance = models.BooleanField(default=False)
    FoodDrink = models.BooleanField(default=False)
    Games = models.BooleanField(default=False)
    Health = models.BooleanField(default=False)
    Travel = models.BooleanField(default=False)
    Parenting = models.BooleanField(default=False)
    Travel = models.BooleanField(default=False)

    def __str__(self):
        return self.email + self.firstname















#    first_name = models.CharField(max_length=40)
    #last_name = models.CharField(max_length=100)

    #def __str__(self):
        #return self.first_name + self.last_name
