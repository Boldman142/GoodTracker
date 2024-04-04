from django.forms import model_to_dict
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import HabitNice, HabitGood
from users.models import User


class HabitGoodTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.ru'
        )
        self.hg = HabitGood.objects.create(
            name='Test',
            owner=self.user,
            place='Testovoe',
            time='00:12:00',
            action='Testi_opyat',
            reward='Nagrada',
            need_time='00:02:00'
        )
        self.hn = HabitNice.objects.create(
            name='Testovoe1',
            owner=self.user,
            action='Dvijnyak'
        )

        self.client.force_authenticate(
            user=self.user
        )

    def test_create_hg(self):
        """Тестирование создание полезной привычки"""
        data = model_to_dict(self.hg, exclude=['connect_habit'])
        response = self.client.post(
            '/habit/good/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_public_hg(self):
        """Тестирование просмотра списка публичных полезных привычек"""
        response = self.client.get(
            '/habit/good/public/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_lesson(self):
        """Тестирование просмотра полезной привычки"""
        response = self.client.get(
            reverse('habit:habit_good_get', args=[self.hg.id])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        """Тестирование изменения полезной привычки"""
        data = {
            "name": "Test new"
        }

        response = self.client.patch(
            reverse('habit:habit_good_update', args=[self.hg.id]), data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_lesson(self):
        """Тестирование удаления урока"""
        data = model_to_dict(self.hg, exclude=['connect_habit'])

        response1 = self.client.post(
            '/habit/good/create/',
            data=data
        )

        response = self.client.delete(
            reverse('habit:habit_good_del', args=[response1.json()['id']])
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
