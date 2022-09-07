from django.urls import path

from .views import PersonListView, PersonDetailView
from .views import PersonCreateView, PersonUpdateView, PersonDeleteView

app_name = 'application'
urlpatterns = [
    path('', PersonListView.as_view(), name='PersonListView'),
    path('create/', PersonCreateView.as_view(), name='PersonCreateView'),
    path('<pk>/', PersonDetailView.as_view(), name='PersonDetailView'),
    path('<pk>/update/', PersonUpdateView.as_view(), name='PersonUpdateView'),
    path('<pk>/delete/', PersonDeleteView.as_view(), name='PersonDeleteView'),
]