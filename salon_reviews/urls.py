from django.urls import path 


from .views import ReviewsListView, ReviewsCreateView, ReviewsDeletelView, ReveiwsDetailView, ReviewsUpdateView

urlpatterns = [
    path('', ReviewsListView.as_view(), name='home'),
    path('review/<int:pk>/', ReveiwsDetailView.as_view(), name='reviewpost_detail'),
    path('review/new/', ReviewsCreateView.as_view(), name='reviewpost_new'),
    path('review/<int:pk>/edit/', ReviewsUpdateView.as_view(), name='reviewpost_edit'),
    path('review/<int:pk>/delete/', ReviewsDeletelView.as_view(), name='reviewpost_delete'),

]