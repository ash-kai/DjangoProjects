from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from .forms import AccountForm, NotificationForm, TaskForm

# Create your views here.

def index(request):
    return render(request, 'ToDo/index.html',{})

def error(request):
    return HttpResponse('You my friend have made an error')

def default(request):
    return HttpResponse("This is the default page")

def success(request):
    return HttpResponse("Your changes have been saved")

def account(request):
    if request.method=='POST':
        form = AccountForm(request.POST)
        if form.is_valid():	    
            form.save()
            return HttpResponseRedirect('success')
        else:
            return HttpResponseRedirect('error')
    else:
        form = AccountForm()
        return render(request, 'ToDo/accounts.html', {'form':form})

def task(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
	print form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success')
        else:	    
            return render(request, 'ToDo/error.html', {'form':form.errors})
    else:
        form = TaskForm()
	date = datetime.now().strftime("%m/%d/%Y")
	time = datetime.now().strftime("%H:%M %p")
        return render(request, 'ToDo/task.html', {'form':form,'date1':date,'time1':time})

def notification(request):
    if request.method=='POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
	    taskTmp = form.save(commit=False)
	    task.created_date = datetime.now()
            taskTmp.save()
            return HttpResponseRedirect('success')
        else:
            return HttpResponseRedirect('error')
    else:
        form = NotificationForm()
        return render(request, 'ToDo/notification.html', {'form':form})

