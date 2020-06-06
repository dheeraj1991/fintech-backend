from django.db import models
# Create your models here.


class Customer(models.Model):
    """
        This model holds the customer data, all fields are mandatory
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
