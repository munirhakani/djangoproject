from django.urls import path

from .views import ObjectDetailView
from .views import ObjectTemplateView, ObjectListView, ObjectDetailView
from .views import ObjectCreateView, ObjectUpdateView, ObjectDeleteView
from .views import ObjectFindView

from .apps import TransactionConfig
app_name = TransactionConfig.name

urlpatterns = [
    path('', ObjectTemplateView.as_view(), name='ObjectTemplateView'),
    path('list/', ObjectListView.as_view(), name='ObjectListView'),
    path('create/', ObjectCreateView.as_view(), name='ObjectCreateView'),
    path('find/', ObjectFindView.as_view(), name='ObjectFindView'),
    path('<pk>/detail/', ObjectDetailView.as_view(), name='ObjectDetailView'),
    path('<pk>/update/', ObjectUpdateView.as_view(), name='ObjectUpdateView'),
    path('<pk>/delete/', ObjectDeleteView.as_view(), name='ObjectDeleteView'),
]