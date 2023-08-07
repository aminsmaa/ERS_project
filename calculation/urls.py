from django.urls import path
from .views import home_view, test_view, ListView, PersonDetailView, updateView,PersonShareView, more_info_view #,CalcView
from . import views
urlpatterns = [
    path('', home_view, name='homePage'),
    # path('Form/', form_view, name='formPage'),
    path('Form/', views.FormCreateView.as_view(), name='formPage'),
    path('Test/', test_view.as_view(), name='testPage'),
    path('List/', ListView.as_view(), name='listPage'),
    path('<int:pk>/', PersonDetailView.as_view(), name='detailPage'),
    path('<int:pk>/update/', views.PersonUpdateView.as_view(), name='person_update'),
    path('<int:pk>/delete/', views.PersonDeleteView.as_view(), name='person_delete'),
    # path('<int:pk>/calc', CalcView.as_view(), name='calcPage'),
    path('<int:pk>/calc', updateView, name='calcPage'),
    path('<int:pk>/share', PersonShareView.as_view(), name='share_view'),
    # path('<int:pk>/calc',calc_view, name='calcPage'),
    path('moreinfo/', more_info_view, name='moreinfo'),

]