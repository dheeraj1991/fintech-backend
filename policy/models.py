from django.db import models
# Create your models here.


class Policy(models.Model):
    """
        This model holds the policy specific data, all fields are mandatory
    """
    premium_type = models.CharField(max_length=100)
    premium = models.FloatField()
    cover = models.FloatField()

    def __str__(self):
        return '{}'.format(self.premium_type)
