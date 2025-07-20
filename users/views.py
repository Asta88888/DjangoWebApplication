from django.contrib.auth.forms import UserChangeForm
from django.views.generic import CreateView, DetailView, UpdateView
from users.forms import UserRegisterForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
from users.models import User


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')


    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)
        return super().form_valid(form)


    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать на сайт!'
        message = 'Спасибо за выбор нашего сайта!'
        from_email = 'asta.soul@yandex.ru'
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)


class UserDetailView(DetailView):
    model = User
    template_name = 'users/user.html'
    context_object_name = 'user'


    def get_object(self):
        return self.request.user


class UserUpdateView(UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users:user')


    def get_object(self):
        return self.request.user
