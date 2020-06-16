from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact, Polls
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(requests):

    return render(requests, 'home.html')


def about(requests):
    return render(requests, 'about.html')


def registrations(requests):
    if requests.method == 'POST':
        try:
            name = requests.POST['name']
            username = requests.POST['username']
            email = requests.POST['email']
            password = requests.POST['password']
            temp_obj = User.objects.create_user(username, email, password)
            temp_obj.first_name = name.split()[0]
            try:
                temp_obj.last_name = name.split()[1]
            except:
                pass
            temp_obj.save()
            messages.success(
                requests, "User Successfully Registered, Try to Log in Now")
        except:
            messages.error(requests, "Username or Email already Registered")
    return render(requests, 'registraitons.html')


def handlelogin(requests):
    if requests.method == 'POST':
        username = requests.POST['username']
        password = requests.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(requests, user)
            messages.success(requests, 'Successfully Logged in')
        else:
            messages.error(requests, 'Invalid username or password')
            return redirect(registrations)
    return redirect(home)


def handlelogout(requests):
    logout(requests)
    messages.success(
        requests, "User Successfully logged out, Have a good day ")
    return redirect(home)


def contact(requests):
    if requests.method == 'POST':
        name = requests.POST['name']
        email = requests.POST['email']
        contact = requests.POST['number']
        subject = requests.POST['subject']
        issue = requests.POST['issue']
        temp_obj = Contact(name=name, email=email,
                           contact_no=contact, subject=subject, issue=issue)
        temp_obj.save()
        messages.success(
            requests, "Thanks For Your Feedback,We Will Reply You soon")
    return render(requests, 'contact.html')


def donate(requests):
    return render(requests, 'donate.html')

@login_required(login_url='/registrations')
def dashboard(requests):
    context = {'polls': Polls.objects.filter(user=requests.user)}
    return render(requests, 'dashboard.html', context)

@login_required(login_url='/registrations')
def detail(requests, id=None):
    if id == None:
        context = {}
        pass
    else:
        required_object = Polls.objects.get(id=id)
        context = {'poll': required_object}
    return render(requests, 'detail_edit_poll.html', context)

@login_required(login_url='/registrations')
def save(requests, id=None):
    question = requests.GET['question']
    decription = requests.GET['decription']
    option1 = requests.GET['option1']
    option2 = requests.GET['option2']
    option3 = requests.GET['option3']
    option4 = requests.GET['option4']
    option5 = requests.GET['option5']
    option6 = requests.GET['option6']
    option7 = requests.GET['option7']
    option8 = requests.GET['option8']
    if id == None:
        temp_obj = Polls(user=requests.user, title=question, decription=decription, option1=option1, option2=option2,
                         option3=option3, option4=option4, option5=option5, option6=option6, option7=option7, option8=option8)
        temp_obj.save()
        messages.success(requests, "Successfully Created")
    else:
        temp_obj = Polls.objects.get(id=id)
        temp_obj.decription = decription
        temp_obj.option1 = option1
        temp_obj.option2 = option2
        temp_obj.option3 = option3
        temp_obj.option4 = option4
        temp_obj.option5 = option5
        temp_obj.option6 = option6
        temp_obj.option7 = option7
        temp_obj.option8 = option8
        temp_obj.save()
        messages.success(requests, "Changes Saved")
    return redirect(dashboard)


def share(requests, id):
    obj = Polls.objects.get(id=id)
    print(obj)
    options = []
    if obj.option1 != "None" and obj.option1!="":
        options.append(obj.option1)
    if obj.option2 != "None" and obj.option2!="":
        options.append(obj.option2)
    if obj.option3 != "None" and obj.option3!="":
        options.append(obj.option3)
    if obj.option4 != "None" and obj.option4!="":
        options.append(obj.option4)
    if obj.option5 != "None" and obj.option5!="":
        options.append(obj.option5)
    if obj.option6 != "None" and obj.option6!="":
        options.append(obj.option6)
    if obj.option7 != "None" and obj.option7!="":
        options.append(obj.option7)
    if obj.option8 != "None" and obj.option8!="":
        options.append(obj.option8)
    context = {'options': options,
               'poll': Polls.objects.get(id=id)
               }
               
    return render(requests, 'vote.html', context)

@login_required(login_url='/registrations')
def delete(requests, id):
    obj = Polls.objects.get(id=id)

    obj.delete()
    messages.success(requests, "Successfully Deleted ")
    return redirect(dashboard)
def votecount(requests,id):
    option=requests.GET['option']
    obj=Polls.objects.get(id=id)
    if obj.option1 == option:
        obj.option1_count+=1 
    if obj.option2 == option:
        obj.option2_count+=1
    if obj.option3 == option:
        obj.option3_count+=1
    if obj.option4 == option:
        obj.option4_count+=1
    if obj.option5 == option:
        obj.option5_count+=1
    if obj.option6 == option:
        obj.option6_count+=1
    if obj.option7 == option:
        obj.option7_count+=1
    if obj.option8 == option:
        obj.option8_count+=1
    obj.save()
    context={}
    return render(requests, 'vote.html', context)
@login_required(login_url='/registrations')
def search(requests):
    query=requests.GET['query']
    polls=Polls.objects.filter(title__contains=query)
    print(len(polls))
    if len(polls)==0:
        messages.info(requests,'Nothing is found, Try Again')
    else:
        messages.info(requests,'Search Results.....')   
    context={'polls':polls}
    return render(requests,'dashboard.html',context)