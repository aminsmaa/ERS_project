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


def more_info_view(request):
    return render(request, 'calculation/moreInfo.html')


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
    # print(str(form_class.Meta.model.author))
    # print(form_class.Meta.model.objects.filter(id=64).values('author'))
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

class PersonShareView(generic.DetailView):
    model = Calculation
    template_name = 'calculation/Share.html'
    context_object_name = 'person'



class PersonUpdateView(generic.UpdateView):
    model = Calculation
    form_class = PersonView
    template_name = 'Calculation/Form.html'


class PersonDeleteView(generic.DeleteView):
    model = Calculation
    template_name = 'calculation/person_delete.html'
    success_url = reverse_lazy('listPage')


# class CalcView(generic.UpdateView):
#     model = Calculation
#     form_class = PersonView
#     model.father_share = 8
#
#     model.father_share = 7
#     Calculation.objects.model.father_share = 9
#     template_name = 'calculation/calc.html'
#     context_object_name = 'person'


def updateView(request, pk):
    person = get_object_or_404(Calculation, pk=pk)

    # restore all shares to zero to calculate again
    person.hamsar_share = 0.0
    person.father_share = 0.0
    person.son_share = 0.0
    person.daughter_share = 0.0
    person.brother_share = 0.0
    person.brother_from_mother_share = 0.0
    person.brother_from_father_share = 0.0
    person.sister_share = 0.0
    person.sister_from_mother_share = 0.0
    person.sister_from_father_share = 0.0
    person.father_of_mother_share = 0.0
    person.father_of_father_share = 0.0
    person.mother_of_father_share = 0.0
    person.mother_of_mother_share = 0.0


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
    if not has_child() and not has_father() and not has_mother() :
                # ----------   grand parents   ----------#
        remain = 1
        if person.singularity != 'sing':
            if person.gender == 'f':
                person.hamsar_share = 1 / 2
            else:
                person.hamsar_share = 1 / 4
            remain = 1 - person.hamsar_share


        if (person.has_grandFather_of_mother == 'Y' or person.has_grandMother_of_mother == 'Y') and \
                (person.has_grandMother_of_father == 'Y' or person.has_grandFather_of_father == 'Y'):

            if person.has_grandFather_of_mother == 'Y' and person.has_grandMother_of_mother == 'Y':
                person.mother_of_mother_share = remain/3 / 2
                person.father_of_mother_share = remain/3 / 2
            elif person.has_grandFather_of_mother == 'Y':
                person.father_of_mother_share = remain/3
            elif person.has_grandMother_of_mother == 'Y':
                person.mother_of_mother_share = remain/3

            if person.has_grandMother_of_father == 'Y' and person.has_grandFather_of_father == 'Y':
                person.father_of_father_share = remain / 3 * 2 / 3 * 2
                person.mother_of_father_share = remain / 3 * 2 / 3
            elif person.has_grandMother_of_father == 'Y':
                person.mother_of_father_share = remain/3*2
            elif person.has_grandFather_of_father == 'Y':
                person.father_of_father_share = remain/3*2

        elif (person.has_grandFather_of_mother == 'N' or person.has_grandMother_of_mother == 'N') and \
                (person.has_grandMother_of_father == 'Y' or person.has_grandFather_of_father == 'Y'):

            if person.has_grandMother_of_father == 'Y' and person.has_grandFather_of_father == 'Y':
                person.mother_of_father_share = remain / 3
                person.father_of_father_share = remain / 3 * 2
            elif person.has_grandMother_of_father == 'Y':
                person.mother_of_father_share = remain
            elif person.has_grandFather_of_father == 'Y':
                person.father_of_father_share = remain

        elif (person.has_grandFather_of_mother == 'Y' or person.has_grandMother_of_mother == 'Y') and \
                (person.has_grandMother_of_father == 'N' or person.has_grandFather_of_father == 'N'):
            if person.has_grandFather_of_mother == 'Y' and person.has_grandMother_of_mother == 'Y':
                person.mother_of_mother_share = remain / 2
                person.father_of_mother_share = remain / 2
            elif person.has_grandFather_of_mother == 'Y':
                person.father_of_mother_share = remain
            elif person.has_grandMother_of_mother == 'Y':
                person.mother_of_mother_share = remain


        else:
                # ----------   siblings   ----------#

            if has_sibling():
                remain = from_mother_share(person, remain)

                if person.number_of_common_sisters == 0 :
                    person.brother_share = remain / person.number_of_common_brothers
                elif person.number_of_common_brothers == 0 :
                    person.sister_share = remain / person.number_of_common_sisters
                elif person.number_of_common_sisters != 0 and person.number_of_common_brothers != 0 :
                    remain = remain / (person.number_of_common_brothers * 2 + person.number_of_common_sisters)
                    person.brother_share = remain * 2
                    person.sister_share = remain

            elif person.number_of_brothers_from_father + person.number_of_sister_from_father != 0:
                remain = from_mother_share(person, remain)

                remain = remain - (person.number_of_common_brothers * 2 + person.number_of_common_sisters)
                person.brother_share = remain * 2
                person.sister_share = remain

    print(person.father_share + person.mother_share + person.hamsar_share + person.son_share*person.number_of_sons + person.daughter_share*person.number_of_daughters)
    person.save()
    return render(request, 'calculation/calc.html', context={'person': person})


def from_mother_share(person, remain):
    if person.number_of_brothers_from_mother + person.number_of_sisters_from_mother == 1:
        if person.number_of_sisters_from_mother == 1:
            person.sister_from_mother_share = remain / 6
        elif person.number_of_brothers_from_mother == 1:
            person.brother_from_mother_share = remain / 6
        remain -= remain / 6
    elif person.number_of_brothers_from_mother + person.number_of_sisters_from_mother > 1:
        rest_share = remain / 3
        if person.number_of_sisters_from_mother == 0:
            person.brother_from_mother_share = rest_share / person.number_of_brothers_from_mother
        elif person.number_of_brothers_from_mother == 0:
            person.sister_from_mother_share = rest_share / person.number_of_sisters_from_mother
        else:
            rest_share = rest_share / (person.number_of_brothers_from_mother +
                                       person.number_of_sisters_from_mother)
            person.brother_from_mother_share = rest_share
            person.sister_from_mother_share = rest_share
        remain = remain / 3 * 2
    return remain
