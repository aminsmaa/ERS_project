from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Calculation


class SitePostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.dead1 = Calculation.objects.create(
            name='artificial User',
            author=cls.user,
            gender='m',
            singularity='hasW',
            has_mother='Y',
            has_father='Y',
            number_of_sons=2,
            number_of_daughters=3,

        )

        # uni tests:

    def test_calculation_list_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
