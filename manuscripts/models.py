import os
import uuid

from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser

from manuscripts.validators import validate_file_size


def file_path(instance, filename):
    file_path = os.path.join(instance.author.media_path, filename)
    return file_path


class Manuscript(models.Model):
    class ManuscriptCategory(models.TextChoices):
        COMPUTER_SCIENCE = 'CS', _('Computer Science')
        ECONOMICS = 'E', _('Economics')
        ELECTRICAL_ENGINEERING = 'EE', _('Electrical Engineering')
        MATHEMATICS = 'M', _('Mathematics')
        PHYSICS = 'P', _('Physics')
        BIOLOGY = 'B', _('Biology')
        FINANCE = 'F', _('Finance')
        STATISTICS = 'S', _('Statistics')
        OTHER = 'O', _('Unknown')

    ALLOWED_EXTENSIONS = ['pdf']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, null=False, blank=False)
    author = models.ForeignKey(CustomUser,
                               on_delete=models.SET_NULL,
                               null=True)
    category = models.CharField(max_length=2,
                                choices=ManuscriptCategory.choices,
                                default=ManuscriptCategory.OTHER)
    file = models.FileField(
        upload_to=file_path,
        validators=[
            FileExtensionValidator(allowed_extensions=ALLOWED_EXTENSIONS),
            validate_file_size
        ],
        null=False,
        blank=False)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
