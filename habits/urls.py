from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, HabitDetailAPIView, HabitUpdateAPIView, HabitDeletePIView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habits_list'),
    path('create/', HabitCreateAPIView.as_view(), name='create_habit'),
    path('<int:pk>/', HabitDetailAPIView.as_view(), name='habit'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(), name='update_habit'),
    path('delete/<int:pk>/', HabitDeletePIView.as_view(), name='delete_habit'),
]
