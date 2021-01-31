from django.urls import path
from . import views, admin

urlpatterns = [
	path('',views.index, name='index'),
	path('task/<int:id>/change/',views.changeTask, name='change task'),
	path('newtask/',views.newTask, name='newtask'),
	path('programs/',views.programs, name='programs'),
	path('employees/',views.employees, name='employees'),
	path('messages/<int:id>/', views.TalkMessages, name='messages'),
]
