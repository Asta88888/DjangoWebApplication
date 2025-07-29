from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from users.models import User


class Command(BaseCommand):
    help = 'Создает группу менеджеры и добавляет пользователей'


    def handle(self, *args, **kwargs):
        group_name = 'Менеджеры'
        group, created = Group.objects.get_or_create(name=group_name)
        if created:
            self.stdout.write(f'Группа "{group_name}" успешно создана')
        else:
            self.stdout.write(f'Группа "{group_name}" уже существует')

        user_emails = ['admin@example.com',]

        for email in user_emails:
            try:
                user = User.objects.get(email=email)
                user.groups.add(group)
                self.stdout.write(f'Пользователь {email} добавлен в группу {group_name}')
            except User.DoesNotExist:
                self.stdout.write(f'Пользователь {email} не найден')
