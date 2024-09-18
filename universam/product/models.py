from django.db import models


class Products(models.Model):
    """
    Продукты:
      Название: С ограничением символов 50.
      Описание: -
      Цена: Максимальное кол-во цифр 8, 2 после запятой.
    """

    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
