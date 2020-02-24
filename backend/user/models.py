from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _

from athlete.models import Athlete
from personal.models import Personal


class UserManager(DjangoUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return super(UserManager, self).create_user(None, email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        return super(UserManager, self).create_superuser(None, email, password, **extra_fields)


class User(AbstractUser):
    username = None
    cpf = models.CharField(verbose_name='CPF', max_length=11, null=False, blank=False)
    email = models.EmailField(_('email address'), unique=True)
    athlete = models.OneToOneField(Athlete, on_delete=models.CASCADE, related_name='user', null=True)
    personal = models.OneToOneField(Personal, on_delete=models.CASCADE, related_name='user', null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
