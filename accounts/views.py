# from django.shortcuts import render
# import django.contrib.auth as auth
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

# def welcome_page_view(request):
#     user_info = auth.get_user_model()
#
#     return render(request, 'accounts/welcome.html')


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
