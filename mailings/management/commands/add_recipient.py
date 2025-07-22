from django.core.management.base import BaseCommand
from mailings.models import Recipient


class Command(BaseCommand):
    help = 'Добавление получателей в базу данных'


    def handle(self, *args, **options):
        recipients_data = [
            {'email': 'asta.soul@yandex.ru', 'full_name': 'Asta Soul', 'comment': 'Первый получатель'},
            {'email': 'admin@example.com', 'full_name': 'Admin Soul', 'comment': 'Второй получатель'}
        ]
        for data in recipients_data:
            recipient, created = Recipient.objects.get_or_create(**data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Создан пололучатель {recipient.email}'))
            else:
                self.stdout.write(self.style.WARNING(f'Получатель {recipient.email} уже существует'))