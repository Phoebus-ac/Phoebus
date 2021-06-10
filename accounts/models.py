import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from accounts.managers import CustomUserManager
from accounts.validators import validate_orcid_id_lenght


class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    email = models.EmailField(_('email address'), unique=True)
    is_certified = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def nickname(self):
        return f'{self.first_name}_{self.last_name}'.lower()

    @property
    def media_path(self):
        timestamp = str(self.date_joined).split(' ')[0]
        directory_name = f'{timestamp}_{self.nickname}'
        return directory_name


class Profile(models.Model):
    class ReputationTiers(models.IntegerChoices):
        BRONZE = 0, 'Bronze'
        SILVER = 1, 'SILVER'
        GOLD = 2, 'GOLD'
        PLATINUM = 3, 'Platinum'
        DIAMOND = 4, 'Diamond'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    email_verified = models.BooleanField(default=False)
    reputation_tier = models.IntegerField(choices=ReputationTiers.choices,
                                          default=ReputationTiers.BRONZE)
    academic_affiliation = models.CharField(max_length=100,
                                            default=None,
                                            null=True,
                                            blank=True)
    academic_affiliation_verified = models.BooleanField(default=False)
    orcid_id = models.CharField(max_length=16,
                                default=None,
                                null=True,
                                blank=True,
                                validators=[validate_orcid_id_lenght])
    orcid_id_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)
