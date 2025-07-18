from django.urls import path
from mailings.apps import MailingsConfig

app_name = MailingsConfig

urlpatterns = [
    path(''),

]
