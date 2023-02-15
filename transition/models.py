from django.db import models


'''Класс Item определяет таблицу в базе данных с тремя полями: name, description и price'''
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField(default=0)
    discount_item = models.ForeignKey('Discount', on_delete=models.SET_NULL, null=True, blank=True,related_name='item_discounts_set')
    tax_item = models.ForeignKey('Tax', on_delete=models.SET_NULL, null=True, blank=True, related_name='item_taxes_set')
    currency = models.CharField(max_length=3, choices=(('usd', 'USD'), ('eur', 'EUR')))

    def __str__(self):
        return self.name

    def discounted_price(self):
        if self.discount_item:
            return self.price - (self.price * self.discount_item.value / 100)
        return self.price

    def tax(self):
        if self.tax_item:
            return self.discounted_price() * self.tax_item.value / 100
        else:
            return 0

    def total(self):
        return self.discounted_price() + self.tax()





class Order(models.Model):
    items = models.ManyToManyField(Item)
    total_price = models.IntegerField(default=0)
    discounted_price = models.IntegerField(default=0)
    currency = models.CharField(max_length=3, choices=(('usd', 'USD'), ('eur', 'EUR')), default='usd')

    def __str__(self):
        return self.name

class Discount(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Tax(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.name


