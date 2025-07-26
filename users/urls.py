from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView, UserDetailView, UserUpdateView, email_verification


app_name = UsersConfig.name


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='mailings:mailing_list'), name='logout'),
    path('user_detail/', UserDetailView.as_view(), name='user_detail'),
    path('user_update/', UserUpdateView.as_view(), name='user_update'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm')
]
