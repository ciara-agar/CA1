from django.urls import path

from .views import RequestListView, RequestDetailView, RequestCreateView, RequestUpdateView, RequestDeleteView

urlpatterns = [
    path('', RequestListView().as_view, name='request_list'),
    path('request/<int:pk>/', RequestDetailView.as_view(), name='request_detail'),
    path('request/new/', RequestCreateView.as_view(), name='request_new'),
    path('request/<int:pk>/edit/', RequestUpdateView.as_view(), name='request_edit'),
    path('request/<int:pk>/delete/', RequestDeleteView.as_view(), name='request_delete'),
]