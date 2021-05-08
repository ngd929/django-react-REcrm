from django.db import models
from django.contrib.auth.models import User

class Property(models.Model):
    mlsId = models.CharField(null=False, max_length=20, default='')
    price = models.CharField(null=False, max_length=20, default='')
    url = models.URLField("URL", blank=True, null=True)
    createdBy = models.ForeignKey(User, related_name='account_created_by', \
                                                on_delete=models.CASCADE)
    isActive = models.BooleanField(default=False)
    thumbnail = models.CharField(max_length=100, blank=True, null=True)
    # agent = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.mlsId
    

class PropertyInfo(Property):
    propertyId = models.CharField(null=False, max_length=20, default='')
    status = models.CharField(null=False, max_length=20, default='')
    history = models.TextField(blank=True, null=True)
    fullAddress = models.TextField(blank=True, null=True)
    yearBuilt = models.CharField(max_length=10, blank=True)
    # property = models.OneToOneField(Property, on_delete=models.CASCADE, \
    #                                         related_name='info')

    def __str__(self):
        return self.propertyId

class Geolocation(models.Model):
    longitude = models.DecimalField(max_digits=10,decimal_places=10, blank=True)
    latitude = models.DecimalField(max_digits=10,decimal_places=10, blank=True)
    property = models.OneToOneField(Property, on_delete=models.CASCADE,related_name="Geo")

class Customer(models.Model):
    firstName = models.CharField("First name", max_length=25, blank = True, null = True)
    lastName = models.CharField("Last name", max_length=25, blank = True, null = True)
    email = models.EmailField(max_length=30, blank = True, null = True)
    phone = models.CharField(max_length=20, blank = True, null = True)
    address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    createdBy = models.ForeignKey(User, related_name='contact_created_by', \
                                            on_delete=models.CASCADE)
    property = models.ManyToManyField(Property)

    def __str__(self):
        return self.firstName + " " + self.lastName