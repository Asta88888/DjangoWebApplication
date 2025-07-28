from django.utils import timezone
from django.core.management import BaseCommand
from django.core.mail import send_mail
from mailings.models import Mailing, MailingAttempt
from config.settings import EMAIL_HOST_USER


class Command(BaseCommand):
    help = 'Отправка рассылки'


    def handle(self, *args, **options):
        active_statuses = ['Создана', 'Запушена']
        mailings = Mailing.objects.filter(status__in=active_statuses)
        for mailing in mailings:
            for recipient in mailing.recipients.all():
                try:
                    send_mail(
                        subject=mailing.message.topic,
                        message=mailing.message.content,
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[recipient.email],
                        fail_silently=False,
                    )
                    MailingAttempt.objects.create(
                        attempt_datetime=timezone.now(),
                        status='Успешно',
                        server_response='Рассылка отправлена',
                        mailing=mailing,
                    )
                except Exception as e:
                    MailingAttempt.objects.create(
                        attempt_datetime=timezone.now(),
                        status='Не успешно',
                        server_response=str(e),
                        mailing=mailing,
                    )
                    print(f'Ошибка отправки {e}')
