# -*- coding: utf-8 -*-
import sys
from time import sleep

from django.core.management.base import BaseCommand, CommandError
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from django.utils import timezone

from apps.posts.models import Post


def get_timezone_aware_datetime(unaware_datetime):
    if unaware_datetime:
        return timezone.make_aware(unaware_datetime, timezone.get_current_timezone())
    else:
        return None


class Command(BaseCommand):
    help = "Import from old db"

    def add_arguments(self, parser):
        parser.add_argument('--activity',
                            action='store_true',
                            dest='activity',
                            default=False,
                            help='Import User Detail')

    def handle(self, *args, **options):
        Base = automap_base()
        engine = create_engine('sqlite:///db.sqlite3.20171129')
        Base.prepare(engine, reflect=True)
        session = Session(engine)

        _Post = Base.classes.posts_post

        posts = session.query(_Post)

        self.stdout.write("Importing Posts...")

        def show_progress(percent):
            sys.stdout.write('\r')
            sys.stdout.write("[%-20s] %d%%" % ('=' * (int(percent / 5)), percent))
            sys.stdout.flush()
            sys.stdout.write("\r")
            sleep(0.25)
        posts_count = posts.count()

        for cnt, post in enumerate(posts):
            _post, post_created = Post.objects.get_or_create(
                title=post.title,
                slug=post.slug,
                image=post.image,
                height_field=post.height_field,
                width_field=post.width_field,
                content=post.content,
                draft=post.draft,
                publish=post.publish,
                read_time=post.read_time,
                updated=post.updated,
                timestamp=post.timestamp,
            )
            _post.save()
            percent = int(float(cnt) * 100 / posts_count)
            show_progress(percent)
        self.stdout.write("Posts data imported")
