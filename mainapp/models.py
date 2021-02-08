import datetime

from django.db import models


"""Статус заказов"""
ORDER_STATUS = (
    ('Новый', 'Новый'),
    ('В обработке', 'В обработке'),
    ('Оплачен', 'Оплачен'),
    ('Доставлено', 'Доставлено')
)


class Product(models.Model):

    """Модель продукта"""
    product_name = models.CharField(max_length=256, verbose_name='Наиминование продукта')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    end_price = models.DecimalField(max_digits=9,
                                    decimal_places=2,
                                    verbose_name="Цена со скидкой",
                                    default=0,
                                    blank=True)
    date = models.DateField(auto_created=True, verbose_name='Дата создания продукта')

    """Метод сохранения скидки"""
    def save(self, *args, **kwargs):
        if self.date < datetime.date.today() - datetime.timedelta(days=30):
            self.end_price = int(self.price - (self.price / 100 * 20))
        else:
            self.end_price = self.price
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product_name}'


class Order(models.Model):

    """Модель заказа"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    status_order = models.CharField(max_length=64,
                                    choices=ORDER_STATUS,
                                    verbose_name='Статус заказа',
                                    default='Новый')
    date_order = models.DateField(auto_created=True, verbose_name='Дата создания заказа')

    def __str__(self):
        return f'{self.product}'


class Score(models.Model):

    """Модель счёта"""
    name = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='name')
    date_score = models.DateField(auto_created=True, verbose_name='Дата создания счёта')

    def __str__(self):
        return f'{self.name}'