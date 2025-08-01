import secrets

from django.shortcuts import get_object_or_404, redirect, reverse
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserUpdateForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
from users.models import User


class RegisterView(CreateView):
    """Представление для регистрации нового пользователя.
    После успешной регистрации отправляет приветственное письмо."""
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """Обрабатывает валидную форму регистрации.
        Сохраняет пользователя и отправляет приветственное письмо после того как пользователь подтвердил почту."""
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(
            subject="Подтверждение почты",
            message=f"Для подтверждения почты перейди по ссылке {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        """Отправляет приветственное письмо на указанный email."""
        subject = 'Добро пожаловать на сайт!'
        message = 'Спасибо за выбор нашего сайта!'
        from_email = EMAIL_HOST_USER
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'

    def get_object(self):
        return self.request.user


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('users:user_list')


class UserDetailView(DetailView):
    """Представление для отображения информации о текущем пользователе.
    Использует текущего авторизованного пользователя."""
    model = User
    template_name = 'users/user_detail.html'
    context_object_name = 'user'

    def get_object(self):
        """Возвращает текущего авторизованного пользователя."""
        return self.request.user


class UserUpdateView(UpdateView):
    """Представление для редактирования данных текущего пользователя.
    После обновления перенаправляет на страницу профиля."""
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users:user_detail')

    def get_object(self):
        """Возвращает текущего авторизованного пользователя для редактирования."""
        return self.request.user
