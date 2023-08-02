from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic

import calculation
from .models import Calculation
from .forms import PersonView
from .admin import PostAdmin
from django.template import loader


def home_view(request):
    context = {
        'page_name': 'Home',

    }
    return render(request, 'calculation/Home.html', context)


# def form_view(request):
#     context = {
#         'page_name' : 'Form',
#
#     }
#     if request.method == 'POST':
#         print(request.POST)
#     return render(request, 'calculation/Form.html', context)

class FormCreateView(generic.CreateView):
    form_class = PersonView
    print(str(form_class.Meta.model.author))
    print(form_class.Meta.model.objects.filter(id=64).values('author'))
    template_name = 'calculation/Form.html'


class test_view(generic.CreateView):
    pass


class ListView(generic.ListView):
    template_name = 'calculation/list.html'
    context_object_name = 'person_list'

    def get_queryset(self):
        return Calculation.objects.order_by('-date_modified')


class PersonDetailView(generic.DetailView):
    model = Calculation
    template_name = 'calculation/person_detail.html'
    context_object_name = 'person'


class PersonUpdateView(generic.UpdateView):
    model = Calculation
    form_class = PersonView
    template_name = 'Calculation/Form.html'


class PersonDeleteView(generic.DeleteView):
    model = Calculation
    template_name = 'calculation/person_delete.html'
    success_url = reverse_lazy('listPage')


class CalcView(generic.UpdateView):
    model = Calculation
    form_class = PersonView
    model.father_share = 8

    model.father_share = 7
    Calculation.objects.model.father_share = 9
    template_name = 'calculation/calc.html'
    context_object_name = 'person'


def updateView(request, pk):
    person = get_object_or_404(Calculation, pk=pk)

    def has_child():
        return False if person.number_of_sons + person.number_of_daughters == 0 else True

    def has_sibling():
        return True if person.number_of_common_sisters + person.number_of_common_brothers != 0 else False

    def has_father():
        return True if person.has_father == 'Y' else False

    def has_mother():
        return True if person.has_mother == 'Y' else False

    if person.singularity == 'hasW':
        person.gender = 'm'
    elif person.singularity == 'hasH':
        person.gender = 'f'
    print(person.gender)

    # ----------   first level   ----------#

    if has_child():
        if has_mother():
            person.mother_share = 1 / 6
        if person.singularity != 'sing':
            if person.gender == 'f':
                person.hamsar_share = 1 / 4
            elif person.gender == 'm':
                person.hamsar_share = 1 / 8

        if person.number_of_sons == 0:
            if person.number_of_daughters == 1:
                person.daughter_share = 1 / 2
                if has_father():
                    person.father_share = 1 - (person.mother_share + person.hamsar_share + person.daughter_share)
                else:
                    person.father_share = 0
                    if has_mother():
                        person.mother_share += 1 - (person.mother_share + person.hamsar_share)

            elif person.number_of_daughters > 1 and not has_mother() and not has_father():
                person.daughter_share = 2 / 3

            elif person.number_of_daughters > 1 and has_mother() and has_father():
                person.father_share = 1 / 6
                person.daughter_share = 1 - (person.father_share + person.mother_share + person.hamsar_share)
                person.daughter_share /= person.number_of_daughters

        else:
            if has_father():
                person.father_share = 1/6
            remaining = 1 - (person.father_share + person.mother_share + person.hamsar_share)
            if person.number_of_daughters == 0:
                person.son_share = remaining / person.number_of_sons
            else:
                division = remaining / (person.number_of_sons * 2 + person.number_of_daughters)
                person.daughter_share = division
                person.son_share = division * 2

    else:  # has no children
        if has_mother():
            person.mother_share = 1 / 3
        if person.singularity != 'sing':
            if person.gender == 'f':
                person.hamsar_share = 1 / 2
            elif person.gender == 'm':
                person.hamsar_share = 1 / 4
        if has_father():
            person.father_share = 1 - (person.mother_share + person.hamsar_share)
        else:
            person.father_share = 0
            if has_mother():
                person.mother_share += 1 - (person.mother_share + person.hamsar_share)



                # ----------   second level   ----------#
    if not has_child() and not has_father() and not has_mother() and person.singularity != 'sing':

        pass







    person.save()
    return render(request, 'calculation/calc.html', context={'person': person})
