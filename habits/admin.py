from django.contrib import admin

from habits.models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'place', 'time', 'action', 'is_pleasant', 'related_habit', 'periodicity', 'reward',
                    'time_to_complete', 'is_public')
    search_fields = ('user', 'place', 'action',)
    list_filter = ('user', 'is_public')
