from django.contrib import admin
from mailings.models import Mailing, Message, Recipient


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'start_datetime', 'end_datetime')
    list_filter = ('name', 'status',)
    search_fields = ('name',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic',)
    list_filter = ('topic',)
    search_fields = ('topic',)


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'full_name', 'comment')
    list_filter = ('email',)
    search_fields = ('email',)
