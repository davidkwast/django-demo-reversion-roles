from django.db import models

from django.utils import timezone

# from django.utils.translation import gettext_lazy as _

# from django.core.mail import send_mail

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

#


class CustomUserManager(BaseUserManager):
    #
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))

        user.set_password(password)

        user.save(using=self._db)

        return user

    #
    def create_superuser(self, email, password=None):
        user = self.create_user(email, password=password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user


#
class User(AbstractBaseUser, PermissionsMixin):
    #
    email = models.EmailField('E-mail', unique=True)
    password = models.CharField('password', max_length=128)

    #
    # Django stuff
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    #
    date_joined = models.DateTimeField('date joined', default=timezone.now)
    last_login = models.DateTimeField('last login', blank=True, null=True)

    #
    # admin stuff
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    #
    # custom fields
    short_name = models.CharField(
        'Short name', max_length=128, blank=True, default=''
    )
    long_name = models.CharField(
        'Full name', max_length=128, blank=True, default=''
    )

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def clean(self):
    #     super().clean()
    #     self.email = self.__class__.objects.normalize_email(self.email)

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)
