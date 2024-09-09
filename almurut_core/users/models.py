from django.contrib.auth.models import AbstractUser
from django.db import models
from users.managers import CustomUserManager

class CustomUser(AbstractUser):
    """Кастомная модель для пользователей"""

    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    email = models.EmailField(unique=True,
                              db_index=True)  # Добавляет индескс в базу данных!

    birth_date = models.DateField(null=True)
    avatar = models.ImageField(upload_to='avatars/')
    phone_number = models.CharField(max_length=30)

    objects = CustomUserManager()


    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'




