from django.db import models
from django.utils import timezone



# Create your models here.

# Задание №1
# Создайте модель для запоминания бросков монеты: орёл или
# решка. Также запоминайте время броска.

# Задание №2
# Доработаем задачу 1.
# Добавьте статический метод для статистики по n последним броскам монеты.
# Метод должен возвращать словарь с парой ключей-значений, для орла и для решки.

class HeadsTails(models.Model):
    objects = None
    rest_time = models.DateTimeField(default=timezone.now)
    res = models.CharField(max_length=50)

    @staticmethod
    def statistic(n):
        n = int(n)
        dict_res = {'Орёл': 0, 'Решка': 0}
        query = list(HeadsTails.objects.all())
        list_res = query[-n:]
        for item in list_res:
            if 'Орёл' in item:
                dict_res['Орёл'] += 1
            elif 'Решка' in item:
                dict_res['Решка'] += 1
        return dict_res

    def __str__(self):
        return f'time: {self.rest_time}, res: {self.res}'
