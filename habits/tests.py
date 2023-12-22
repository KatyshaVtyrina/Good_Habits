
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


class HabitValidatorsTestCase(APITestCase):
    """Тестирование валидаторов модели Habit"""
    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@example.com', password='test')
        self.client.force_authenticate(user=self.user)

        self.habit_is_pleasant = Habit.objects.create(
            user=self.user,
            place='Test',
            time='12:00:00',
            action='Test',
            is_pleasant=True,
            periodicity=1,
            time_to_complete='00:00:30',
            is_public=True,
        )

        self.habit_is_not_pleasant = Habit.objects.create(
            user=self.user,
            place='Test',
            time='12:00:00',
            action='Test',
            is_pleasant=False,
            periodicity=1,
            time_to_complete='00:00:30',
            reward='Test',
            is_public=True,
        )

    def test_create_validate_related_habit_or_reward(self):
        """Проверка исключения при одновременном указании связанной привычки и вознаграждения при создании объекта"""
        new_habit = {
            "place": "Test",
            "time": "12:00:00",
            "action": "Test",
            "is_pleasant": False,
            "periodicity": 1,
            "time_to_complete": "00:00:30",
            "reward": "Test",
            "related_habit": self.habit_is_pleasant.pk
        }

        response = self.client.post(
            path='/habits/create/',
            data=new_habit
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {
                'non_field_errors': [
                    'Нельзя указывать одновременно связанную привычку и вознаграждение']
            }
        )

    def test_update_validate_related_habit_or_reward(self):
        """Проверка исключения при одновременном указании связанной привычки и вознаграждения при обновлении объекта"""

        update_data = {
            "related_habit": self.habit_is_pleasant.pk
        }

        update_response = self.client.patch(
            path=f'/habits/update/{self.habit_is_not_pleasant.pk}/',
            data=update_data
        )

        self.assertEqual(
            update_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            update_response.json(),
            {
                'non_field_errors': [
                    'Нельзя указывать одновременно связанную привычку и вознаграждение']
            }
        )

    def test_validate_time_to_complete(self):
        """Проверка времени выполнения привычки"""
        update_data = {
            "time_to_complete": "00:05:00"
        }

        update_response = self.client.patch(
            path=f'/habits/update/{self.habit_is_pleasant.pk}/',
            data=update_data
        )

        self.assertEqual(
            update_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            update_response.json(),
            {
                'non_field_errors': [
                    'Время выполнения не может быть более двух минут']
            }
        )

    def test_validate_related_habit_is_pleasant(self):
        """Проверка связанной привычки на признак приятной привычки"""
        update_data = {
            "related_habit": self.habit_is_not_pleasant.pk
        }

        update_response = self.client.patch(
            path=f'/habits/update/{self.habit_is_pleasant.pk}/',
            data=update_data
        )

        self.assertEqual(
            update_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            update_response.json(),
            {
                'non_field_errors': [
                    'В связанные привычки могут попадать только привычки с признаком приятной привычки.']
            }
        )

    def test_create_validate_is_pleasant(self):
        """Проверка наличия вознаграждения и/или связанной привычки у приятной привычки при создании объекта"""
        new_habit = {
            "place": "Test",
            "time": "12:00:00",
            "action": "Test",
            "is_pleasant": True,
            "periodicity": 1,
            "time_to_complete": "00:00:30",
            "reward": "Test"
        }

        response = self.client.post(
            path='/habits/create/',
            data=new_habit
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            response.json(),
            {
                'non_field_errors': [
                    'У приятной привычки не может быть вознаграждения или связанной привычки.']
            }
        )

    def test_update_validate_is_pleasant(self):
        """Проверка наличия вознаграждения и/или связанной привычки у приятной привычки при обновлении объекта"""

        update_data = {
            "reward": "Test"
        }

        update_response = self.client.patch(
            path=f'/habits/update/{self.habit_is_pleasant.pk}/',
            data=update_data
        )

        self.assertEqual(
            update_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            update_response.json(),
            {
                'non_field_errors': [
                    'У приятной привычки не может быть вознаграждения или связанной привычки.']
            }
        )

    def test_validate_periodicity(self):
        """Проверка периодичности, не может быть реже, чем 1 раз в 7 дней."""
        update_data = {
            "periodicity": 8
        }

        update_response = self.client.patch(
            path=f'/habits/update/{self.habit_is_pleasant.pk}/',
            data=update_data
        )

        self.assertEqual(
            update_response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertEqual(
            update_response.json(),
            {
                'non_field_errors': [
                    'Нельзя выполнять привычку реже, чем 1 раз в 7 дней.']
            }
        )
