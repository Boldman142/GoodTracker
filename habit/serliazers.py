from rest_framework import serializers

from habit.models import HabitGood, HabitNice


class HabitGoodSerializer(serializers.ModelSerializer):

    class Meta:
        model = HabitGood
        fields = '__all__'


class HabitNiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = HabitNice
        fields = '__all__'
