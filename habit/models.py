from django.db import models

from users.models import NULLABLE


class HabitGood(models.Model):
    name = models.CharField(max_length=50, verbose_name='название для привычки')
    owner = models.ForeignKey('users.User', verbose_name='владелец',
                              on_delete=models.CASCADE, **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место')
    time = models.TimeField(verbose_name='во сколько')
    action = models.CharField(max_length=150, verbose_name='действие')

    connect_habit = models.ForeignKey('habit.HabitNice', on_delete=models.SET_NULL,
                                      verbose_name='приятная привычка',
                                      **NULLABLE)
    reward = models.TextField(verbose_name='вознаграждение', **NULLABLE)

    period = models.PositiveSmallIntegerField(default=1, verbose_name='1 раз, во сколько дней повторять',
                                              **NULLABLE)

    need_time = models.TimeField(verbose_name='сколько времени займет')
    public = models.BooleanField(default=False, verbose_name='видно ли всем')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Полезная привычка'
        verbose_name_plural = 'Полезные привычки'


class HabitNice(models.Model):
    name = models.CharField(max_length=50, verbose_name='название для привычки')
    owner = models.ForeignKey('users.User', verbose_name='владелец',
                              on_delete=models.CASCADE, **NULLABLE)

    action = models.TextField(verbose_name='действие')

    need_time = models.TimeField(verbose_name='сколько времени займет')
    public = models.BooleanField(default=False, verbose_name='видно ли всем')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приятная привычка'
        verbose_name_plural = 'Приятные привычки'
