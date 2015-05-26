from django.db import models

# Create your models here.
class Size(models.Model):
    size = models.CharField(max_length=255,default="size")
    country = models.CharField(max_length=255,default="country")

    class Meta:
        db_table = 'size'


class Order(models.Model):
    user_id = models.IntegerField(default = 5)
    size = models.ForeignKey(Size)

    class Meta:
        db_table = 'orders'
