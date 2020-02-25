from django.contrib.auth.models import AbstractUser, UserManager as DjangoUserManager
from django.db import models
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _


class State(models.Model):
    name = models.CharField(_('name'), null=False, blank=False, max_length=30, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['name'], name='state_name_idx'),
        ]

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(_('name'), null=False, blank=False, max_length=40)
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name=_('state'), null=False, blank=False)

    class Meta:
        unique_together = ['name', 'state']
        indexes = [
            models.Index(fields=['name'], name='city_name_idx'),
        ]

    def __str__(self):
        return self.name


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
    MALE = 'M'
    FEMALE = 'F'
    SEX_TYPES = (
        (MALE, _('Male')),
        (FEMALE, _('Female'))
    )
    username = None

    # Personal information
    national_id = models.CharField(_('identification'), max_length=18, null=False, blank=False, unique=True)
    email = models.EmailField(_('email address'), max_length=320, unique=True)
    birthday = models.DateField(_('birthday'), null=False, blank=False)
    phone_number = models.CharField(_('phone number'), null=False, blank=False, max_length=15)
    city = models.ForeignKey(City, on_delete=models.PROTECT, verbose_name=_('city'), null=False, blank=False)
    sex = models.CharField(_('sex'), null=False, blank=False, max_length=1, choices=SEX_TYPES)

    # Control system information
    slug = models.SlugField(_('slug'), max_length=320, null=False, blank=True, unique=True)
    is_athlete = models.BooleanField(_('is athlete?'), default=False)
    is_trainer = models.BooleanField(_('is trainer?'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.email)
        return super().save(*args, **kwargs)
