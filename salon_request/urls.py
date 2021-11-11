from django.urls import path

from .views import RequestListView

urlpatterns = [
    path('', RequestListView(), name='request')
]