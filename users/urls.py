from django.urls import path
from users.apps import UsersConfig
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView, UserDetailView, UserUpdateView


app_name = UsersConfig.name


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='mailings:mailing_list'), name='logout'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name='user_update'),
]
