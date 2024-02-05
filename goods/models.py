from django.db import models


class Good(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length = 255, verbose_name = 'Заголовок')
    price = models.IntegerField(default = 0, verbose_name = 'Цена')
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
         return self.title