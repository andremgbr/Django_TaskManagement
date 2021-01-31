from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Programs(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Employees(models.Model):
	HIERARCHY_CHOICE = (
		('cl','Concept_Leader'),
		('pl','Program_leader'),
		('fl','FB_leader'),
		('dl','Direct_leader'),
		('ds','Desingner'),

		)
	name = models.CharField(max_length=40)
	hierarchy = models.CharField(max_length=2, choices=HIERARCHY_CHOICE)
	code_number = models.CharField(max_length=10)
	user_web = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.name

	def natural_key(self):
		return (self.name)


class Task(models.Model):
	SITUATION_CHOICE = (
	('pg','Em progresso'),
	('fl','Finalizado'),
	('al','Em análise'),
	('cl','Cancelado'),

	)

	name = models.CharField(max_length=100)
	program = models.ForeignKey(Programs, on_delete=models.CASCADE)
	requested_employ_id = models.ForeignKey(Employees,related_name='requested_employ_id',null=True , on_delete=models.CASCADE)
	info = models.TextField(max_length=1000)
	is_filed = models.BooleanField(null=True)
	situation = models.CharField(max_length=2, choices = SITUATION_CHOICE,null=True)

	def __str__(self):
		return self.name


class DestinationTask(models.Model):
	task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
	destination_employ_id = models.ForeignKey(Employees,related_name='destination_employ_id', null=True , on_delete=models.CASCADE)


class Message(models.Model):
	text = models.TextField()
	owner = models.ForeignKey(Employees, on_delete=models.CASCADE)
	task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)