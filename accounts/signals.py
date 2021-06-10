import logging

import os

from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import CustomUser

from Phoebus.settings.base import MEDIA_ROOT

logger = logging.getLogger('backend')


@receiver(post_save, sender=CustomUser)
def create_user(sender, instance, created, **kwargs):
    if created:
        if not instance.is_superuser:
            logger.info('Running custom functions at user creation...')
            user_media_path = os.path.join(MEDIA_ROOT, instance.media_path)
            try:
                logger.info('Creating a media directory for user...')
                os.makedirs(user_media_path)
                logger.info('Media directory for user created!')
            except Exception as e:
                message = ('Failed to create media directory for user. '
                           f'Reason: {str(e)}.')
                logger.warning(message)
            logger.info('Custom functions at user creation done!')
