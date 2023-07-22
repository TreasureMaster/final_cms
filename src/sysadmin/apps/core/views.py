# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
# from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import UserCreationForm, SendForm


def index(request):
    """Тестовая страница для редактиования фронта"""
    return render(
        request,
        'base.html',
        {'cards': [1, ]}
    )


# @login_required
# def dashboard(request):
#     return render(
#         request,
#         'accounts/dashboard.html',
#     )


class SignUp(CreateView):
    """Create account"""
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


def message_send(request):
    if request.method == 'POST':
        form = SendForm(request.POST)
        if form.is_valid():
            # Отправить письмо
            # return HttpResponseRedirect('/thanks/')
            form = SendForm()
            messages.success(request, 'Ваше сообщение успешно отправлено!')
            send_mail(
                request.POST['subject'],
                request.POST['text'],
                'Алексей админ <am5x86p75@list.ru>',
                # ['am5x86p75@list.ru'],
                [request.POST['email']],
                # fail_silently=False
            )
        else:
            messages.error(request, 'Ошибка во введенных данных')

    else:
        form = SendForm()

    return render(request, 'base.html', {'form': form, 'cards': [1]})
