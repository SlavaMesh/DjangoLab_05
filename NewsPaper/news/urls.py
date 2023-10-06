from django.urls import path
from .views import NewsList, PostDetail, SearchList, ADD, Delete, Update


urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', SearchList.as_view()),
    path('add/', ADD.as_view(), name='post_add'),
    path('<int:pk>/delete/', Delete.as_view(), name='post_delete'),
    path('<int:pk>/edit/', Update.as_view(), name='post_update')
]

