from django.db import models

# Create your models here.
class Table(models.Model):
    name = models.CharField(max_length=4)
    already_ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    category_id = models.PositiveIntegerField()
    tax = models.BooleanField(default=True)
    price = models.PositiveIntegerField()
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
class OrderProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=0)

class Order(models.Model):
    table = models.ForeignKey(Table, blank=True, null=True, verbose_name='table', on_delete=models.PROTECT)
    date = models.DateTimeField(blank=True, null=True)
    order_products = models.ManyToManyField(OrderProduct)

    def __str__(self):
        return '{} ({})'.format(self.table, self.date)