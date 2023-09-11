from django import forms

from django.contrib.auth import forms as auth_forms
from django.contrib.auth.forms import PasswordResetForm

from .crispy_helpers import SignupFormHelper, SenderFormHelper


class UserCreationForm(auth_forms.UserCreationForm):
    """class extension"""
    class Meta(auth_forms.UserCreationForm.Meta):
        fields = ('username', 'email')
        field_classes = {
            'username': auth_forms.UsernameField,
            'email': forms.EmailField,
        }

    def __init__(self, *args, **kwargs):
        # сохранение запроса HttpRequest внутри формы
        # self.request = request
        super().__init__(*args, **kwargs)
        self.helper = SignupFormHelper()


class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']

        from django.contrib.auth.models import User
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            msg = (
                "There is no user registered with the specified E-Mail address."
            )
            self.add_error('email', msg)
        return email


class SendForm(forms.Form):
    name = forms.CharField(label='Введите ваше имя (опционально)', max_length=100, required=False)
    email = forms.EmailField(label='Укажите email для отправки сообщения')
    subject = forms.CharField(label='Укажите тему сообщения', max_length=50)
    text = forms.CharField(label='Напишите ваше сообщение', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        # сохранение запроса HttpRequest внутри формы
        # self.request = request
        super().__init__(*args, **kwargs)
        self.helper = SenderFormHelper()


# class SendForm2(forms.Form):
#     name = forms.CharField(max_length=100, required=False)
#     email = forms.EmailField()
#     subject = forms.CharField(max_length=50)
#     text = forms.CharField()
