import logging
from django.core.management.base import BaseCommand

from hn_rest_api.models import Post

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        posts = Post.objects.all()
        for post in posts:
            post.up_votes_amount = 0
            post.save()

        logger.info('Posts vote reset')
        print('ready')
