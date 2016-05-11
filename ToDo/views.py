from django.shortcuts import render
from .models import Task
from django.http import HttpResponseRedirect, HttpResponse

from .forms import AccountForm

# Create your views here.

def index(request):
    latest_task = Task.objects.order_by('Due Date')
    return HttpResponse("JHey watss up")

def create_Task(request):
    pass

def error(request):
    return HttpResponse('You my friend have made an error')

def default(request):
    return HttpResponse("This is the default page")

def HelloUser(request):
    if request.method=='POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('Got it')
        else:
            return HttpResponseRedirect('error')
    else:
        form = AccountForm()
        return render(request, 'ToDo/hey.html', {'form':form})

def Hey(request):
    '''
    if 'YName' in request.POST:
	value = request.POST.get('YName')
	return HttpResponse("Welcome "+value)
    else:
	return HttpResponse("Nope not working")
    '''
    data = request.POST    
    answer = ''
    for key in data.keys():
	answer+=key+' : '+data[key]+'\n'
    return HttpResponse("Hey " + answer)
