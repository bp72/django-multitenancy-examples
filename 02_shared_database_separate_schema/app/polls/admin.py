from django.contrib import admin
from .models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    ...


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    ...
