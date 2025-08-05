from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from mailings.models import Mailing, Message, Recipient, MailingAttempt
from mailings.forms import MailingForm, RecipientForm, MessageForm
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


@method_decorator(cache_page(60*10), name='dispatch')
class MailingListView(LoginRequiredMixin, ListView):
    """Представление для отображения списка всех рассылок."""
    model = Mailing
    permission_required = 'mailings.list_mailing'

    def get_queryset(self):
        if self.request.user.has_perm('mailings.list_mailing'):
            return Mailing.objects.all()
        return Mailing.objects.filter(owner=self.request.user)


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Представление для отображения деталей конкретной рассылки."""
    model = Mailing
    permission_required = 'mailings.detail_mailing'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not (obj.owner == self.request.user or self.request.user.has_perm('mailings.detail_mailing')):
            raise PermissionDenied
        return obj


class MailingCreateView(LoginRequiredMixin, CreateView):
    """Представление для создания новой рассылки."""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')
    permission_required = 'mailings.create_mailing'

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()
        return super().form_valid(form)


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление для редактирования существующей рассылки."""
    model = Mailing
    form_class = MailingForm
    success_url = reverse_lazy('mailings:mailing_list')
    permission_required = 'mailings.change_mailing'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied
        return obj


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление для удаления рассылки."""
    model = Mailing
    success_url = reverse_lazy('mailings:mailing_list')
    permission_required = 'mailings.delete_mailing'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied
        return obj


@method_decorator(cache_page(60*10), name='dispatch')
class RecipientListView(LoginRequiredMixin, ListView):
    """Представление для отображения списка всех получателей."""
    model = Recipient
    permission_required = 'mailings.list_recipient'

    def get_queryset(self):
        if self.request.user.has_perm('mailings.list_recipient'):
            return Recipient.objects.all()
        return Recipient.objects.filter(owner=self.request.user)


class RecipientDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Представление для отображения деталей конкретного получателя."""
    model = Recipient
    permission_required = 'mailings.detail_recipient'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not (obj.owner == self.request.user or self.request.user.has_perm('mailings.detail_recipient')):
            raise PermissionDenied
        return obj


class RecipientCreateView(LoginRequiredMixin, CreateView):
    """Представление для добавления нового получателя."""
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailings:recipient_list')
    permission_required = 'mailings.create_recipient'

    def form_valid(self, form):
        recipient = form.save()
        user = self.request.user
        recipient.owner = user
        recipient.save()
        return super().form_valid(form)


class RecipientUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление для редактирования информации о получателе."""
    model = Recipient
    form_class = RecipientForm
    success_url = reverse_lazy('mailings:recipient_list')
    permission_required = 'mailings.change_recipient'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied
        return obj


class RecipientDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление для удаления получателя."""
    model = Recipient
    success_url = reverse_lazy('mailings:recipient_list')
    permission_required = 'mailings.delete_recipient'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied
        return obj


@method_decorator(cache_page(60*10), name='dispatch')
class MessageListView(LoginRequiredMixin, ListView):
    """Представление для отображения списка сообщений."""
    model = Message
    permission_required = 'mailings.list_message'

    def get_queryset(self):
        if self.request.user.has_perm('mailings.list_message'):
            return Message.objects.all()
        return Message.objects.filter(owner=self.request.user)


class MessageDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """Представление для просмотра деталей сообщения."""
    model = Message
    permission_required = 'mailings.detail_message'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not (obj.owner == self.request.user or self.request.user.has_perm('mailings.detail_message')):
            raise PermissionDenied
        return obj


class MessageCreateView(LoginRequiredMixin, CreateView):
    """Представление для создания нового сообщения."""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()
        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """Представление для редактирования сообщения."""
    model = Message
    form_class = MessageForm
    success_url = reverse_lazy('mailings:message_list')
    permission_required = 'mailings.change_message'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied
        return obj


class MessageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """Представление для удаления сообщения."""
    model = Message
    success_url = reverse_lazy('mailings:message_list')
    permission_required = 'mailings.delete_message'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user:
            raise PermissionDenied
        return obj


class MailingAttemptListView(LoginRequiredMixin, ListView):
    model = MailingAttempt
    template_name = 'mailings/mailing_attempt.html'
    context_object_name = 'mailing_attempt'


@login_required
def main_page(request):
    """Обрабатывает запрос к главной странице сайта. Собирает статистику по: количеству всех рассылок,
    количеству активных рассылок (со статусом 'Запущена'),
    количеству уникальных получателей. Передает эти данные в шаблон для отображения.
    Возвращает: HttpResponse с шаблоном 'main.html' с контекстом."""
    user = request.user
    total_mailings = Mailing.objects.filter(owner=user).count()
    active_mailings = Mailing.objects.filter(owner=user, status='Запущена').count()
    total_recipients = Recipient.objects.filter(owner=user).count()
    context = {
        'total_mailings': total_mailings,
        'active_mailings': active_mailings,
        'total_recipients': total_recipients,
    }
    return render(request, 'mailings/main.html', context)


def send_mailings(request):
    from mailings.management.commands.send_message import Command as SendMailCommand
    command = SendMailCommand()
    command.handle()

    messages.success(request, "Рассылка запущена.")
    return redirect('mailings:mailing_list')
