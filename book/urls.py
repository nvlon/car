from django.urls import path
from . import views
urlpatterns = [
	path('hello/', views.hello_world, name = 'hello' ),
	path('posts/', views.book_all, name='posts'),

]
