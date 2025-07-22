from django.core.management.base import BaseCommand
from mailings.models import Mailing, Message
from django.utils import timezone


class Command(BaseCommand):
    help = "Добавление рассылки и сообщений в базу данных"


    def handle(self, *args, **options):
        messages_data = [
            {'topic': 'Камчатка', 'content': 'Камчатка стоит посещения благодаря своей уникальной природе: активным вулканам, гейзерам, термальным источникам и дикому животному миру. Это место, где можно увидеть захватывающие пейзажи, от горных вершин до морских побережий, и испытать незабываемые приключения, такие как восхождение на вулканы, рыбалка или сплав по рекам.'},
            {'topic': 'Карелия', 'content': 'Карелия стоит посещения из-за своей уникальной природы: живописные озера, реки, леса и горы, а также исторические и культурные достопримечательности, такие как остров Кижи и горный парк Рускеала.'},
            {'topic': 'Крым', 'content': 'Крым стоит посетить из-за его уникального сочетания природных красот, богатой истории и культурного разнообразия. Полуостров предлагает разнообразные ландшафты: от гор и степей до субтропических лесов и живописного побережья. Здесь можно найти как тихие уединенные места, так и курорты с развитой инфраструктурой. Кроме того, Крым славится своими целебными климатом, историческими достопримечательностями и вкусной местной кухней.'},
        ]
        messages = {}
        for data in messages_data:
            message, created = Message.objects.get_or_create(**data)
            messages[message.topic] = message
            if created:
                self.stdout.write(self.style.SUCCESS(f'Создано сообщение: {message.topic}'))
            else:
                self.stdout.write(self.style.WARNING(f'Сообщение {message.topic} уже существует'))

        mailings = [
            {'name': 'Теплый климат', 'message': messages['Крым']},
            {'name': 'Холодный климат', 'message': messages['Карелия']},
            {'name': 'Необычные места', 'message': messages['Камчатка']},
        ]

        for mailing_data in mailings:
            mailing_data['start_datetime'] = timezone.now()
            mailing_data['end_datetime'] = timezone.now() + timezone.timedelta(days=7)
            mailing, created = Mailing.objects.get_or_create(**mailing_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Создана рассылка: {mailing.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Рассылка {mailing.name} уже существует'))
