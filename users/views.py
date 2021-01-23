from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CreationForm, ContactForm
from django.core.mail import send_mail


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("signup")
    template_name = "signup.html"


send_mail(
    'Тема письма',
    'Текст письма.',
    'from@example.com',
    ['to@example.com'],
    fail_silently=False,
)


'''
Проверка авторизации, ограничение возможностей
@authorized_only
'''


def authorized_only(func):
    def check_user(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        return redirect('/auth/login/')
    return check_user


def user_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['body']
            form.save()
            return redirect('thank-you')
        return render(request, 'contact.html', {'form': form})
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def thankyou(request):
    return render(request, 'thankyou.html')
