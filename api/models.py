from django.contrib.auth.models import AbstractUser
from django.db import models
from model_utils.models import TimeStampedModel


class User(AbstractUser):
    is_verified = models.BooleanField(verbose_name='User Verified', default=False)
    photo_url = models.URLField(verbose_name='Photo Url', blank=True)
    full_name = models.CharField(max_length=256, verbose_name='Full name', blank=True)
    sex_choices = (('M', "Male"), ("F", "Female"))
    sex = models.CharField(max_length=10, verbose_name='Sex', choices=sex_choices, null=True)
    # REQUIRED_FIELDS = ['password', 'full_name']


class Story(TimeStampedModel):
    picture = models.URLField(verbose_name='Status Picture Url')
    caption = models.CharField(max_length=256, verbose_name='Caption')

    def save(self, *args, **kwargs):
        super(Story, self).save(*args, **kwargs)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stories = models.ManyToManyField(Story, verbose_name='Stories')
    # interests = models.
