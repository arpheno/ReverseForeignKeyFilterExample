from django.db import models

# Create your models here.
class Size(models.Model):
    id = models.IntegerField(primary_key=True)
    size = models.CharField(max_length=255,default="size")
    country = models.CharField(max_length=255,default="country")

    class Meta:
        db_table = 'size'


class Orders(models.Model):
    id = models.IntegerField(unique=True,primary_key=True)
    order_id = models.CharField(max_length=255)
    date = models.DateTimeField()
    status = models.CharField(max_length=1)
    brand_id = models.IntegerField()
    user_id = models.IntegerField(default = 6)
    shop_id = models.IntegerField()
    item_id = models.IntegerField()
    category_id = models.IntegerField()
    item_gender = models.CharField(max_length=1)
    return_reason = models.CharField(max_length=255)
    size = models.ForeignKey(Size)

    class Meta:
        db_table = 'orders'
