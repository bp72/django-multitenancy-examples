from django.contrib import admin
from .models import Tenant, Question, Choice


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    ...


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    ...


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    ...
