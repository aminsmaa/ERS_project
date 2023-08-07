from django import forms

from .models import Calculation

class PersonView(forms.ModelForm):
    class Meta:
        model = Calculation
        fields = ['name', 'author', 'gender', 'has_mother', 'has_father', 'singularity', 'number_of_sons',
                  'number_of_daughters','number_of_common_brothers', 'number_of_common_sisters',
                  'number_of_brothers_from_father', 'number_of_sister_from_father',
                  'number_of_brothers_from_mother', 'number_of_sisters_from_mother',
                  'has_grandFather_of_father', 'has_grandMother_of_father',
                  'has_grandFather_of_mother', 'has_grandMother_of_mother',


                  ]