from django.shortcuts import render, redirect, reverse
from . models import Task, Employees, Programs, DestinationTask, Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
import time
from django.http import JsonResponse
import json

# Create your views here.



def index(request):
	if request.user.is_anonymous :
		return redirect('/login/')

	elif request.user.is_superuser:
		return redirect('/admin/')
	
	else:
		current_user = request.user		
		employ = Employees.objects.get(user_web_id=current_user.id)
		dest_list = DestinationTask.objects.filter(destination_employ_id=employ)
		task =[]
		for item in dest_list:
			task.append(item.task_id)
		task_from_user = Task.objects.filter(requested_employ_id=employ)
		return render(request, 'concept/index.html',{'task':task,'user':current_user,'employ':employ,'task_from_user':task_from_user})


def changeTask(request, id):
	if request.user.is_anonymous :
		return redirect('/login/')

	else:
		current_user = request.user
		employ = Employees.objects.get(user_web_id=current_user.id)

		if request.method == 'POST':

			if request.POST.get('save') == 'Save':
				print('clicou em Save')
				task = Task.objects.get(id=id)
				task.info = request.POST.get('info')
				task.save()
				print(request.POST.get('sit'))
				task.situation = request.POST.get('sit')
				task.save()
				return redirect('/')

			elif request.POST.get('Chat') == 'Enviar':
				print('clicou em chat!')
				message = Message(text=request.POST['message'],owner=Employees.objects.get(user_web_id=request.user.id),task=Task.objects.get(id=id))
				message.save()
				return redirect('/task/%s/change/' % id)

		task = Task.objects.get(id=id)
		return render(request, 'concept/changeTask.html',{'user':current_user,'employ':employ,'task':task,'id':id,})

def newTask(request):
	if request.user.is_anonymous :
		return redirect('/login/')

	else:
		program = Programs.objects.all()
		current_user = request.user
		c_employ = Employees.objects.get(user_web_id=current_user.id)
		all_employ = Employees.objects.all()
		all_employ_json = serializers.serialize('json',Employees.objects.all(), fields=('name'))

		if request.method == 'POST':
			name_task = request.POST.get('name_task')
			info = request.POST.get('info')
			prog = request.POST.get('program')
			new = Task(name=name_task,info=info,program=Programs.objects.get(id=prog),requested_employ_id=c_employ)
			new.save()
			employ_list = request.POST.getlist('select_employ')
			employ_list = list(dict.fromkeys(employ_list))
			
			for i in employ_list:
				dest = DestinationTask(task_id=new,destination_employ_id=Employees.objects.get(name=i))
				dest.save()

		return render(request, 'concept/newTask.html',{'user':current_user,'employ':c_employ,'program':program,'all_employ':all_employ_json})



def programs(request):
	if request.user.is_anonymous :
		return redirect('/login/')

	else:
		task = Task.objects.all()
		prog = Programs.objects.all()
		return render(request,'concept/programs.html',{'task':task, 'prog':prog})

def employees(request):
	if request.user.is_anonymous :
		return redirect('/login/')

	else:
		task = Task.objects.all()
		employ_all = Employees.objects.all()
		dest = DestinationTask.objects.all()
		return render(request,'concept/employees.html',{'employ_all':employ_all,'dest':dest,})


def TalkMessages(request,id):
	if request.user.is_anonymous :
		return redirect('/login/')

	else:
		messages = Message.objects.filter(task=Task.objects.get(id=id)).order_by('-created_at')
		results = []

		for message in messages:
			result = [message.text, str(naturaltime(message.created_at)), message.owner.name]
			results.append(result)
		results_json = json.dumps(results)
		return JsonResponse(results_json, safe=False)