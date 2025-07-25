from django.views.generic import CreateView, DetailView, UpdateView
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
        Сохраняет пользователя и отправляет приветственное письмо."""
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)


    def send_welcome_email(self, user_email):
        """Отправляет приветственное письмо на указанный email."""
        subject = 'Добро пожаловать на сайт!'
        message = 'Спасибо за выбор нашего сайта!'
        from_email = 'asta.soul@yandex.ru'
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)


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
