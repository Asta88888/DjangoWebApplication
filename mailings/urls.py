from django.urls import path
from mailings.apps import MailingsConfig
from mailings.views import MailingListView, MailingDetailView, MailingCreateView, MailingUpdateView, MailingDeleteView, MessageListView, MessageDetailView, MessageCreateView, MessageUpdateView, MessageDeleteView, RecipientListView, RecipientDetailView, RecipientCreateView, RecipientUpdateView, RecipientDeleteView

app_name = MailingsConfig

urlpatterns = [
    path('mailings/mailing_list', MailingListView.as_view(), name='mailing_list'),
    path('mailings/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailings/create', MailingCreateView.as_view(), name='mailing_create'),
    path('mailings/<int:pk>/update', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailings/<int:pk>/delete', MailingDeleteView.as_view(), name='mailing_delete'),
    path('mailings/message_list', MessageListView.as_view(), name='message_list'),
    path('mailings/message/<int:pk>', MessageDetailView.as_view(), name='message_detail'),
    path('mailings/message/create', MessageCreateView.as_view(), name='message_create'),
    path('mailings/message/<int:pk>/update', MessageUpdateView.as_view(), name='message_update'),
    path('mailings/message/<int:pk>/delete', MessageDeleteView.as_view(), name='message_delete'),
    path('mailings/recipient_list', RecipientListView.as_view(), name='recipient_list'),
    path('mailings/recipient/<int:pk>', RecipientDetailView.as_view(), name='recipient_detail'),
    path('mailings/recipient/create', RecipientCreateView.as_view(), name='recipient_create'),
    path('mailings/recipient/<int:pk>/update', RecipientUpdateView.as_view(), name='recipient_update'),
    path('mailings/recipient/<int:pk>/delete', RecipientDeleteView.as_view(), name='recipient_delete'),

]
