from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Student(models.Model):
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    avatar = models.ImageField(upload_to='students/', verbose_name='Аватар', **NULLABLE)
    email = models.CharField(max_length=150, verbose_name='почта', unique=True, **NULLABLE)

    is_active = models.BooleanField(default=True, verbose_name='Учится')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        ordering = ('last_name',)


class Subject(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='студент')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'предмет'
        verbose_name_plural = 'предметы'
