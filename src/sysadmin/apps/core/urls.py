# from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views


app_name = 'core'


urlpatterns = [
    # path('dashboard/', views.dashboard, name='dashboard'),
    # Custom auth paths
    # path('signup/', views.SignUp.as_view(), name='signup'),
    # Django auth paths
    # accounts/login/ [name='login']
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change/done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset/done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']
    # path(
    #     'password_reset/',
    #     auth_views.PasswordResetView.as_view(
    #         form_class=EmailValidationOnForgotPassword
    #     ),
    #     name='password_reset'
    # ),
    # path('', views.index, name='index'),
    # NOTE первый вариант
    # path('', views.message_send, name='index'),
    # NOTE второй вариант
    path('', views.message_send2, name='index2'),
    # path('', include('django.contrib.auth.urls')),
]
