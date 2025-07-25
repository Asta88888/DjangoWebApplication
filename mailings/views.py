from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from mailings.models import Mailing, Message, Recipient
from mailings.forms import MailingForm, RecipientForm, MessageForm


class MailingListView(ListView):
    """Представление для отображения списка всех рассылок."""
    model = Mailing


class MailingDetailView(DetailView):
    """Представление для отображения деталей конкретной рассылки."""
    model = Mailing


class MailingCreateView(CreateView):
    """Представление для создания новой рассылки."""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')


class MailingUpdateView(UpdateView):
    """Представление для редактирования существующей рассылки."""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')


class MailingDeleteView(DeleteView):
    """Представление для удаления рассылки."""
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')


class RecipientListView(ListView):
    """Представление для отображения списка всех получателей."""
    model = Recipient


class RecipientDetailView(DetailView):
    """Представление для отображения деталей конкретного получателя."""
    model = Recipient


class RecipientCreateView(CreateView):
    """Представление для добавления нового получателя."""
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailings:recipient_list')


class RecipientUpdateView(UpdateView):
    """Представление для редактирования информации о получателе."""
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailings:recipient_list')


class RecipientDeleteView(DeleteView):
    """Представление для удаления получателя."""
    model = Recipient
    success_url = reverse_lazy('mailings:recipient_list')


class MessageListView(ListView):
    """Представление для отображения списка сообщений."""
    model = Message


class MessageDetailView(DetailView):
    """Представление для просмотра деталей сообщения."""
    model = Message


class MessageCreateView(CreateView):
    """Представление для создания нового сообщения."""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')


class MessageUpdateView(UpdateView):
    """Представление для редактирования сообщения."""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')


class MessageDeleteView(DeleteView):
    """Представление для удаления сообщения."""
    model = Message
    success_url = reverse_lazy('mailings:message_list')