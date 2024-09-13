from django.contrib.auth import login, logout
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser



class LoginView(TemplateView):
    template_name = 'login.html'

class UserMakeLogoutViewt(View):
    """Вью, чтобы выйти из аккаунта"""

    def post(self, request, *args, **kwargs):
        logout(request)
        return render(request, 'login.html')







class UserMakeLogin(View):
    """Вью чтобы залогинить пользователя!"""

    def post(self, request, *args, **kwargs):
        data = request.POST
        email_address = data['email_address']
        password = data['password']

        user = CustomUser.objects.get(email=email_address)
        print('Пользователь', user)

        correct = user.check_password(password)
        print('Коррекст равен', correct)

        if correct == True:
            login(request, user)
            return render(request, 'login.html', context={"logged_in": True})
        else:
            return render(request, 'login.html', context={'logged_in': False})













class UserRegisterView(TemplateView):
    template_name = 'register.html'




class UserMakeRegistrationView(View):
    """Вью. Чтобы зарегестрировать пользователя!"""
    def post(self, request, *args, **kwargs):
        data = request.POST
        password1 = data['password1']
        password2 = data['password2']

        if password1 == password2:
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            user = CustomUser.objects.create_user(email=email,
                                                  password=password2,
                                                  first_name=first_name,
                                                  last_name=last_name
                                                  )
            return render(request, 'product-list.html')
        else:
            pass





