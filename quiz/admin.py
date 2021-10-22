from django.contrib import admin
from django.db import models
from . import models

# Register your models here.
admin.site.register(models.Category)
admin.site.register(models.Quizzes)
admin.site.register(models.Question)
admin.site.register(models.Answer)

class CatAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

class QuizAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
    ]

class AnswerInlineModel(admin.TabularInline):
    model = models.Answer
    fields = [
        'answer_text',
        'is_right',
    ]

class QuestionAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'quiz',
    ]
    list_display = [
        'title',
        'quiz',
    ]
    inlines = [
        AnswerInlineModel,
    ]

class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        'answer_text',
        'is_right',
        'question',
    ]