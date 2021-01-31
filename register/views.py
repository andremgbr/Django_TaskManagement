from django.shortcuts import render, redirect
from .forms import RegisterForm, EmployForm
from concept.models import Employees
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == "POST":
    	Rform = RegisterForm(request.POST)
    	Eform = EmployForm(request.POST)
    	if Rform.is_valid() and Eform.is_valid():
    		Rform.save()
    		name = request.POST.get('name')
    		hierarchy = request.POST.get('hierarchy')
    		username = request.POST.get('username')
    		username = User.objects.get(username=str(username))
    		em = Employees(name=str(name),hierarchy=str(hierarchy),code_number=str(username),user_web= username)
    		em.save()
    		return redirect("/login")
    else:
    	Rform = RegisterForm()
    	Eform = EmployForm()
    	return render(request, "register/register.html", {"Rform":Rform, "Eform":Eform})