from rest_framework import serializers

from habit.models import HabitGood, HabitNice
from habit.validators import PeriodValidator, TimeValidator, ChooseValidator


class HabitGoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitGood
        fields = '__all__'
        validators = [PeriodValidator(field='period'), TimeValidator(field='need_time'),
                      ChooseValidator(field1='connect_habit', field2='reward')]


class HabitNiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitNice
        fields = '__all__'
