from django.shortcuts import render, get_object_or_404
from .models import Task, UserProfile, Notification
from django.http import HttpResponseRedirect, HttpResponse
from datetime import datetime
from .forms import AccountForm, NotificationForm, TaskForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'ToDo/index.html',{})

def error(request):
    return HttpResponse('You my friend have made an error')

def default(request):
    return HttpResponse("This is the default page") 

def success(request):
    return render(request, "ToDo/result.html", {})

def account(request):
    if request.method=='POST':
        form = AccountForm(request.POST)
        if form.is_valid():     
            form.save()
            return HttpResponseRedirect('success')
        else:
            return render(request,'ToDo/accounts.html', {'form':form})
    else:
        form = AccountForm()
        return render(request, 'ToDo/accounts.html', {'form':form})

@login_required
def task(request):
    print "Task Details"
    details = Task.objects.all()
    print details
    context = {
    'title':'Task Details',
    'objects':details,
    }
    return render(request, 'ToDo/detail.html', context)

@login_required
def task_create(request):
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


@login_required
def notification(request):
    print "Notification Details"
    details = Notification.objects.all()
    context = {
    'title':'Notification Types',
    'objects':details,
    }
    return render(request, 'ToDo/detail.html', context)    

@login_required
def notification_create(request):
    print "Notifciation form"
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


@login_required
def notification_update(request, id=None):
    print "Notificaiton Update"
    instance = get_object_or_404(Notification, id=id)
    form = NotificationForm(request.POST or None, instance=instance)
    if request.method=='POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Item successfully Updated")
            return HttpResponseRedirect('success')
        else:
            messages.error(request, "Item not Updated")
            return HttpResponseRedirect('success')
    
    return render(request, 'ToDo/notification.html', {'form':form})

@login_required
def notification_delete(request, id=None):
    instance = get_object_or_404(Notification, id=id)
    instance.delete()
    messages.success(request, "Notificaiton Deleted")
    return render(request,'ToDo/index.html',{})

def profile_create(request):
    registered = False
    if request.method=='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            print type(user), user.__dict__
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'phone_number' in profile.__dict__.keys():
                print "phone number is given"
            profile.save()
            registered = True
            print "Profile  is saved"
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        return render(request, 'ToDo/profile.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})

#Need to work on this part

def profile_update(request, id=None):
    instance = get_object_or_404(UserProfile, id=id)    
    form = UserProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    user_form = form.UserForm
    profile_form = form.UserProfileForm
    registered = False
    return render(request, 'ToDo/profile.html', {'user_form':user_form, 'profile_form':profile_form, 'registered':registered})


def user_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                print "login successful"
                return HttpResponseRedirect('/ToDo/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            print "Invalid login details {0}, {1}".format(username, password)
            return render(request, 'ToDo/login.html',{'error':'Invalid login details supplied'})
    else:
        return render(request, 'ToDo/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'ToDo.index.html', {})
