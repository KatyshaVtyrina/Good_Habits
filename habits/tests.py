
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@example.com', password='test')
        self.client.force_authenticate(user=self.user)

        self.habit = Habit.objects.create(
            user=self.user,
            place='Test',
            time='12:00:00',
            action='Test',
            is_pleasant=False,
            periodicity=1,
            time_to_complete='00:00:30',
            is_public=True,
        )

    def test_create_habit(self):
        """Тестирование создания привычки"""
        data = {
            "place": "Test",
            "time": "12:00:00",
            "action": "Test",
            "is_pleasant": False,
            "periodicity": 1,
            "time_to_complete": "00:00:30",
        }

        response = self.client.post(
            path='/habits/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habits(self):
        """Тестирование вывода списка привычек"""

        response = self.client.get(
            path='/habits/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Habit.objects.all().count(),
            1
        )

    def test_retrieve_habit(self):
        """Тестирования детальной информации о привычке"""
        response = self.client.get(
            path=f'/habits/{self.habit.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": self.habit.pk,
                "user": self.user.pk,
                "place": "Test",
                "time": "12:00:00",
                "action": "Test",
                "is_pleasant": False,
                "related_habit": None,
                "periodicity": 1,
                "reward": None,
                "time_to_complete": "00:00:30",
                "is_public": True
            }
        )

    def test_update_habit(self):
        """Тестирование обновления привычки"""
        data = {
            "place": 'test_update'
        }

        response = self.client.patch(
            path=f'/habits/update/{self.habit.pk}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['place'],
            data['place']
        )

    def test_destroy_habit(self):
        """Тестирование удаления привычки"""
        response = self.client.delete(
            path=f'/habits/delete/{self.habit.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_public_habits(self):
        data = {
            "place": "Test",
            "time": "12:00:00",
            "action": "Test",
            "is_pleasant": False,
            "periodicity": 1,
            "time_to_complete": "00:00:30",
        }

        self.client.post(
            path='/habits/create/',
            data=data
        )

        response = self.client.get(
            path='/habits/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Habit.objects.all().count(),
            2
        )

        self.assertEqual(
            Habit.objects.all().filter(is_public=True).count(),
            1
        )
