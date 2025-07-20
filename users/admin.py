from django.contrib import admin
from users.models import User


@admin.register(User)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
