from django.urls import path
from .views import ProviderListCreate

urlpatterns = [
    path('providers/',ProviderListCreate.as_view(),name='provider-list-create')
]
