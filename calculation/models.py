from django.db import models
from django.shortcuts import reverse


class Calculation(models.Model):
    STATUS_SINGULARITY = (
        ('sing', 'single'),
        ('hasW', 'hasWife'),
        ('hasH', 'hasHusband'),
    )

    YN_CHOICE = (
        ('Y', 'yes'),
        ('N', 'no'),
    )

    GENDER = (
        ('m', 'male'),
        ('f', 'female')
    )

    name = models.CharField(max_length=100)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, max_length=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    has_mother = models.CharField(choices=YN_CHOICE, max_length=1, default='N')
    has_father = models.CharField(choices=YN_CHOICE, max_length=1, default='N')
    has_grandFather_of_father = models.CharField(choices=YN_CHOICE, max_length=1, default='N')
    has_grandMother_of_father = models.CharField(choices=YN_CHOICE, max_length=1, default='N')
    has_grandFather_of_mother = models.CharField(choices=YN_CHOICE, max_length=1, default='N')
    has_grandMother_of_mother = models.CharField(choices=YN_CHOICE, max_length=1, default='N')
    singularity = models.CharField(choices=STATUS_SINGULARITY, max_length=4)
    number_of_sons = models.PositiveSmallIntegerField(default=0)
    number_of_daughters = models.PositiveSmallIntegerField(default=0)
    number_of_common_brothers = models.PositiveSmallIntegerField(default=0)
    number_of_common_sisters = models.PositiveSmallIntegerField(default=0)
    number_of_brothers_from_father = models.PositiveSmallIntegerField(default=0)
    number_of_sister_from_father = models.PositiveSmallIntegerField(default=0)
    number_of_brothers_from_mother = models.PositiveSmallIntegerField(default=0)
    number_of_sisters_from_mother = models.PositiveSmallIntegerField(default=0)

    father_share = models.FloatField(default=0)
    mother_share = models.FloatField(default=0)
    son_share = models.FloatField(default=0)
    daughter_share = models.FloatField(default=0)
    brother_share = models.FloatField(default=0)
    brother_from_mother_share = models.FloatField(default=0)
    sister_from_mother_share = models.FloatField(default=0)
    sister_from_father_share = models.FloatField(default=0)
    brother_from_father_share = models.FloatField(default=0)
    sister_share = models.FloatField(default=0)
    hamsar_share = models.FloatField(default=0)
    bro_of_dad_share = models.FloatField(default=0)
    sis_of_dad_share = models.FloatField(default=0)
    bro_of_mom_share = models.FloatField(default=0)
    sis_of_mom_share = models.FloatField(default=0)
    father_of_father_share = models.FloatField(default=0)
    mother_of_father_share = models.FloatField(default=0)
    father_of_mother_share = models.FloatField(default=0)
    mother_of_mother_share = models.FloatField(default=0)

    def __str__(self):
        return f'{self.name}'


    def get_absolute_url(self):
        return reverse('detailPage', args=[self.id])