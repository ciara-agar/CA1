from django.urls import path 


from .views import ReviewsListView, ReviewsDetailView, ReviewsCreateView, ReviewsUpdateView, ReviewsDeleteView

urlpatterns = [
    path('', ReviewsListView.as_view(), name='home'),
    path('review/<int:pk>/', ReviewsDetailView.as_view(), name='reviewpost_detail'),
    path('review/new/', ReviewsCreateView.as_view(), name='reviewpost_new'),
    path('review/<int:pk>/edit/', ReviewsUpdateView.as_view(), name='reviewpost_edit'),
    path('review/<int:pk>/delete/', ReviewsDeleteView.as_view(), name='reviewpost_delete'),

]