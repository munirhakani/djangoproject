from django.urls import path

from .views import PersonTemplateView, PersonListView, PersonDetailView
from .views import PersonCreateView, PersonUpdateView, PersonDeleteView

app_name = 'application'
urlpatterns = [
    path('', PersonTemplateView, name='PersonTemplateView'),
    path('list/', PersonListView, name='PersonListView'),
    path('create/', PersonCreateView, name='PersonCreateView'),
    path('<pk>/', PersonDetailView, name='PersonDetailView'),
    path('<pk>/update/', PersonUpdateView, name='PersonUpdateView'),
    path('<pk>/delete/', PersonDeleteView, name='PersonDeleteView'),
]