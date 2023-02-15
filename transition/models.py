from django.db import models


"""
Модели для управления товарами, заказами, скидками и налогами.

Class Item:
    Модель товара с полями:
    - name: название товара
    - description: описание товара
    - price: цена товара
    - discount_item: связь с моделью скидок Discount, по умолчанию null и blank
    - tax_item: связь с моделью налогов Tax, по умолчанию null и blank
    - currency: валюта товара

    Методы:
    - discounted_price: возвращает цену товара со скидкой, если присутствует
    - tax: возвращает сумму налога для данного товара
    - total: возвращает общую стоимость товара с учетом скидки и налога

Class Order:
    Модель заказа с полями:
    - items: связь многие-ко-многим с моделью Item
    - total_price: общая стоимость заказа
    - discounted_price: общая стоимость заказа со скидкой
    - currency: валюта заказа

Class Discount:
    Модель скидки с полями:
    - name: название скидки
    - value: размер скидки в процентах

Class Tax:
    Модель налога с полями:
    - name: название налога
    - value: размер налога в процентах
"""

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


