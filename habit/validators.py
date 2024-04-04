from datetime import datetime, timedelta

from rest_framework.serializers import ValidationError


class PeriodValidator:
    """Валидатор того, что повторения будут не реже 1 раза в неделю"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if not tmp_val:
            return
        if tmp_val > 7:
            raise ValidationError('Привычку надо выполнять не реже 1 раза в неделю')


class ChooseValidator:
    """Валидатор того, в награду будет либо приятная привычка, либо вознаграждение
    (или вообще ничего)"""

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        tmp_val1 = dict(value).get(self.field1)
        tmp_val2 = dict(value).get(self.field2)
        if not (tmp_val1 and tmp_val2):
            return
        if bool(tmp_val1) and bool(tmp_val2):
            raise ValidationError('Выбери либо приятную привычку, либо вознаграждение')


class TimeValidator:
    """Валидатор того, что время, требуемое на привычку было не больше 120 секунд"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if not tmp_val:
            return
        time_user = timedelta(hours=tmp_val.hour, minutes=tmp_val.minute, seconds=tmp_val.second)
        time = timedelta(minutes=2)
        if time_user > time:
            raise ValidationError('Время выполнения должно быть не больше 120 секунд')
