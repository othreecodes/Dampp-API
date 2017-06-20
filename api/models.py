from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_verified = models.BooleanField(verbose_name='User Verified', default=False)
    photo_url = models.URLField(verbose_name='Photo Url', blank=True)
    full_name = models.CharField(max_length=256, verbose_name='Full name', blank=True)

    REQUIRED_FIELDS = ['password', 'full_name']
