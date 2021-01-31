from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):


	class Meta:
		model = User
		fields = ["username", "password1", "password2"]

class EmployForm(forms.Form):
	HIERARCHY_CHOICE = (
		('cl','Concept_Leader'),
		('pl','Program_leader'),
		('fl','FB_leader'),
		('dl','Direct_leader'),
		('ds','Desingner'),

	)

	name = forms.CharField(max_length=40)
	hierarchy = forms.ChoiceField(choices = HIERARCHY_CHOICE)