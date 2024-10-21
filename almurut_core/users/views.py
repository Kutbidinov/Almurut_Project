from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


class UserRegistrationView(TemplateView):
    template_name = 'register.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'


class UserMakeLogoutView(View):
    """Вью, чтобы выйти из аккаунта"""

    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'login.html')


class UserMakeLoginView(View):
    """Вью, чтобы залогинить пользователя"""

    def post(self, request, *args, **kwargs):
        data = request.POST
        email = data['email_address']
        password = data['password']

        user = CustomUser.objects.get(email=email)
        print('пользователь ', user)

        correct = user.check_password(password)
        print('коррект равен ', correct)

        if correct == True:
            login(request, user)
            return render(request, 'login.html', context={'logged_in': True})
        else:
            return render(request, 'login.html', context={'logged_in': False})






class UserMakeRegistrationView(View):
    """Вью, чтобы зарегистрировать пользователя"""

    def post(self, request, *args, **kwargs):
        data = request.POST

        password1 = data['password1']
        password2 = data['password2']

        if password1 == password2:
            blabla = data['first_name']
            last_name = data['last_name']
            email = data['email_address']
            user = CustomUser.objects.create_user(
                email=email, password=password1,
                first_name=blabla, last_name=last_name,
            )
            return render(request, 'product-list.html')
        else:
            pass
            # TODO: вызови ошибку для клиента,  о том что пароль подтверждения не совппадаемт