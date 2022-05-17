from datetime import datetime

from django.test import TestCase
from core.tests import (object_title, object_slug, object_description,
                        object_contents, object_published_date)

from .models import Organogram


class UserPolygonTestCase(TestCase):

    def setUp(self):
        Organogram.objects.create(
            title=object_title,
            slug=object_slug,
            description=object_description,
            contents=object_contents,
            publishing_date=object_published_date,
        )

    def test_organogram_details(self):
        object = Organogram.objects.get(id=1)
        self.assertEqual(object.title, object_title)
        self.assertEqual(object.header_image, '')
        self.assertEqual(object.updating_date.date(), datetime.now().date())
