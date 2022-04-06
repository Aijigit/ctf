from pyexpat import model
from statistics import mode
from django.db import models
import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
class Category(models.Model):
    name = models.CharField(verbose_name='Название категории', max_length=60)
    def __str__(self):
        return self.name


class Difficulty(models.Model):
    name = models.CharField(verbose_name='Сложность', max_length=40)
    def __str__(self):
        return self.name

class Task(models.Model):
    FIRST_LEVEL = 'FT_LV'
    SECOND_LEVEL = 'SC_LV'
    THIRD_LEVEL = 'TH_LV'
    LEVELS_CHOICES = [
        (FIRST_LEVEL, 'Уровень-1'),
        (SECOND_LEVEL, 'Уровень-2'),
        (THIRD_LEVEL, 'Уровень-3'),
    ]
    title = models.TextField(verbose_name='Текст задачи', max_length=255)
    difficulty = models.ForeignKey(Difficulty, on_delete=models.PROTECT, verbose_name='Сложность задачи')
    point = models.SmallIntegerField(verbose_name='Количество баллов')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория задачи')
    level = models.CharField(max_length=5, choices=LEVELS_CHOICES, default=FIRST_LEVEL)
    number_of_flag = models.SmallIntegerField(verbose_name='Количество флагов')
    hint = models.TextField(verbose_name='Подсказки')
    def __str__(self):
        return self.title


class Flag_Check(models.Model):
    task = models.ForeignKey(Task, verbose_name='Задача', on_delete=models.PROTECT)
    flag = models.CharField(verbose_name='Флаг', max_length=200)
    def __str__(self):
        return self.flag


class Group(models.Model):
    name = models.CharField(verbose_name='Группа', max_length=20)
    class Meta:
        managed = False

class Student(models.Model):
    full_name = models.CharField(verbose_name='ФИО', max_length=60)
    group = models.ForeignKey(Group, verbose_name='Группа', on_delete=models.PROTECT)
    username = models.CharField(verbose_name='Логин', max_length=30, unique=True)
    password = models.CharField(verbose_name='Пароль', max_length=150)

class St_Task(models.Model):
    student = models.ForeignKey(Student, verbose_name='Студент', on_delete=models.PROTECT)
    task = models.ForeignKey(Task, verbose_name='Задача', on_delete=models.PROTECT)
    point = models.SmallIntegerField()


