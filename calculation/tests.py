from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

from .models import Calculation


class SitePostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user1')
        cls.dead1 = Calculation.objects.create(
            name='artificial Person',
            author=cls.user,
            gender='m',
            singularity='hasW',
            has_mother='Y',
            has_father='Y',
            number_of_sons=2,
            number_of_daughters=3,

        )



    def test_person_model_str(self):
        person = self.dead1
        self.assertEqual(str(person), person.name)


    def test_person_detail(self):
        person = self.dead1
        self.assertEqual(person.name, 'artificial Person')
        self.assertEqual(person.singularity, 'hasW')

        # uni tests:

    def test_calculation_list_url(self):
        response = self.client.get('/List/')
        self.assertEqual(response.status_code, 200)

    def test_calculation_list_url_by_name(self):
        response = self.client.get(reverse('listPage'))
        self.assertEqual(response.status_code, 200)

    def test_calculation_name_on_list_page(self):
        response = self.client.get(reverse('listPage'))
        self.assertContains(response, self.dead1.name)


    def test_person_detail_url_by_name(self):
        response = self.client.get(reverse('detailPage', args=[self.dead1.id]))
        self.assertEqual(response.status_code, 200)

    def test_person_detail_url(self):
        response = self.client.get(f'/{self.dead1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_person_detail_on_detail_page(self):
        response = self.client.get(reverse('detailPage',args=[self.dead1.id]))
        self.assertContains(response, self.dead1.name)
        # self.assertEqual(response, self.dead1.author)

    def test_status_404_person_not_exist(self):
        response = self.client.get(reverse('detailPage', args=[999]))
        self.assertEqual(response.status_code, 404)


    def test_create_view(self):
        response = self.client.post(reverse('formPage'), {
            'name' : 'not real person',
            'author' : self.user.id,
            'singularity' : 'sing',
            'gender' : 'm'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Calculation.objects.last().name, 'not real person')
        self.assertEqual(Calculation.objects.last().author, self.user.username)


    def test_update_view(self):
        response = self.client.post(reverse('person_update', args=[self.dead1.id]), {
            'name' : 'updated name',
            'author' : self.user.id,
            'singularity' : 'sing',
            'gender' : 'm'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Calculation.objects.last().name, 'updated name')
        self.assertEqual(Calculation.objects.last().singularity, 'hasW')


    def test_delete_view(self):
        response = self.client.post(reverse('person_delete', args=[self.dead1.id]))
        self.assertEqual(response.status_code, 302)