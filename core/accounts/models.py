from django.db import models
from django.urls import reverse

class VisibileManager(models.Manager):
    def get_queryset(self):
        return super(VisibileManager,
                     self) \
                     .get_queryset()\
                     .filter(visible=True)
class Listing(models.Model):

    address = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    postal = models.IntegerField()
    price = models.FloatField()
    description = models.CharField(max_length=500)
    bathroom_count = models.FloatField(max_length=250)
    bedroom_count = models.IntegerField()
    square_footage = models.IntegerField()
    # property_type = models.CharField(max_length=250)
    property_type = models.ForeignKey('accounts.Property_Type', on_delete=models.CASCADE)
    # subdivision = models.CharField(max_length=250)
    subdivision = models.ForeignKey('accounts.Subdivision', on_delete=models.CASCADE)
    # prop_status = models.CharField(max_length=250)
    prop_status = models.ForeignKey('accounts.Prop_Status', on_delete=models.CASCADE)
    visible = models.BooleanField()
    featured = models.BooleanField()
    objects = models.Manager()
    isVisible = VisibileManager()

    def __str__(self):
        return self.address

    def get_absolute_url(self):
        return reverse('accounts:listing_detail',
                       args=[self.id])

class Property_Type(models.Model):
    prop_type_name = models.CharField(max_length=30)
    prop_type_descr = models.CharField(max_length=100)

    def __str__(self):
        return self.prop_type_name

class Prop_Status(models.Model):
    prop_status = models.CharField(max_length=20)
    prop_status_descr = models.CharField(max_length=100)

    def __str__(self):
        return self.prop_status

class Subdivision(models.Model):
    subdiv_name = models.CharField(max_length=50)
    subdiv_descr = models.CharField(max_length=100)

    def __str__(self):
        return self.subdiv_name

