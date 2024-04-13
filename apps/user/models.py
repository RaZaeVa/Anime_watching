from django.db import models
from django.contrib.auth.models import AbstractBaseUser

from apps.user.managers import MyUserManager


class User(AbstractBaseUser):
    username = models.CharField(
        max_length=123,
        unique=True
    )
    email = models.EmailField(
        unique=True,
        blank=False,
        null=False
    )
    password = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    phone_number = models.CharField(
        max_length=13,
        unique=True
    )
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Обычный пользователь'),
            (2, 'Менеджер')
        ),
        default=1
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )

    is_admin = models.BooleanField(
        default=False
    )
    is_active = models.BooleanField(
        default=True
    )

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        """Is the user a member of staff?"""
        # Simplest possible answer: All admins are staff
        return self.is_admin
