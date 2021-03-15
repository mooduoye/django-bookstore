from django.urls import path
from .views import HomeView, BookList,book_detail

urlpatterns = [
    path('home/', HomeView.as_view(),name='home'),
    path('', BookList.as_view(),name='ebook'),
    path('<slug:slug>',book_detail,name='book-detail')

]