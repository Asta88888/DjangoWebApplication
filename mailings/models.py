from django.utils import timezone
from django.db import models


class Messages(models.Model):
    topic = models.CharField(max_length=100, verbose_name='Тема письма')
    content = models.TextField(max_length=500, verbose_name='Содержание письма')


    def __str__(self):
        return self.topic


    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Recipient(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    full_name = models.CharField(max_length=100, verbose_name='Ф.И.О')
    comment = models.TextField(max_length=500, verbose_name='Комментарий')


    def __str__(self):
        return f'{self.full_name} - {self.email}'


    class Meta:
        verbose_name = 'Получатель рассылки'
        verbose_name_plural = 'Получатели рассылки'



class Mailing(models.Model):
    STATUS_CHOICES = [
        ('Создана', 'Создана'),
        ('Запушена', 'Запушена'),
        ('Завершена', 'Завершена'),
    ]
    name = models.CharField(max_length=100, verbose_name='Название рассылки')
    start_datetime = models.DateTimeField(verbose_name='Дата и время первой отправки')
    end_datetime = models.DateTimeField(verbose_name='Дата и время окончания отправки')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Создана', verbose_name='Статус')
    message = models.ForeignKey(Messages, on_delete=models.CASCADE, related_name='mailing', verbose_name='Сообщение')
    recipients = models.ManyToManyField(Recipient, related_name='mailing', verbose_name='Получатели')


    def __str__(self):
        return f'Рассылка {self.id} - {self.name} - {self.status}'


    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
        ordering = ['status', 'name']


class MailingAttempt(models.Model):
    STATUS_CHOICES = [
        ('Успешно', 'Успешно'),
        ('Не успешно', 'Не успешно'),
    ]
    attempt_datetime = models.DateTimeField(default=timezone.now, verbose_name='Дата и время попытки рассылки')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name='Статус')
    server_response = models.TextField(blank=True, null=True, verbose_name='Ответ сервера')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='attempts', verbose_name='Рассылка')


    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
