from django.shortcuts import render,redirect,get_object_or_404
from .forms import NewUserCreationForm,PropertyCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate,logout
from .models import Account,Property
from django.db import IntegrityError
from django.contrib import messages
from django.http import HttpResponseNotFound,HttpResponseBadRequest
from django.db.models import Q

def front(request):
    properties = Property.objects.all()
    return render(request,'templates/places/landing_page.html',{'property':properties})

def register_(request):
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            cl_data = form.cleaned_data
            user = User(username=cl_data['username'],first_name=cl_data['first_name'],last_name=cl_data['last_name'],email=cl_data['email'])
            user.set_password(cl_data['password'])
            user.save()
            acc = Account(user=user)
            acc.save()
            try:
                login(request,user)
                return redirect('Front')
            except AssertionError:
                messages.error(request,'Assertion Error')
                return redirect('Register-Page')
            except IntegrityError:
                messages.error(request,'User Already Exists.')
                return redirect('Register-Page')
        else:
            return HttpResponseBadRequest('Unclean Data')
    else:
        print('HERE')
        form = NewUserCreationForm()
    return render(request=request,template_name='registration/register.html',context={'form':form})

def login_(request):
    if request.method == 'POST':
        uname = request.POST['username']
        passw = request.POST['password']
        user = authenticate(request=request,username=uname,password=passw)
        if user is not None:
            try:
                login(request=request,user=user)
                return redirect('Front')
            except AssertionError:
                messages.error(request,'Assertion Error')
                return redirect('Login-Page')
            except IntegrityError:
                messages.error(request,'User Already Exists.')
                return redirect('Login-Page')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('Login-Page')
    else:
        form = AuthenticationForm()
    return render(request=request,template_name='registration/login.html',context = {'form':form})
            
@login_required
def createProperty(request):
    if request.method == 'POST':
        form = PropertyCreationForm(request.POST,request.FILES)
        if form.is_valid():
            cl_data = form.cleaned_data
            p1 = Property(
                name=cl_data['name'],
                description=cl_data['description'],
                price=cl_data['price'],
                image=cl_data['image'],
                square_foot=cl_data['square_foot'],
                location=cl_data['location'],
                bhk=cl_data['bhk'],
                additional_bhk=cl_data['additional_bhk'],
            )
            p1.save()
            return redirect('Front')
        else:
            return redirect(HttpResponseBadRequest('Invalid Form'))
    else:
        form = PropertyCreationForm()
    return render(request=request,template_name='templates/places/create_property.html',context={'form':form})

def viewProperty(request,id):
    prop = get_object_or_404(Property,pk=id)
    return render(request=request,template_name='templates/places/property_page.html',context={'property':prop})

@login_required
def purchaseProperty(request,id):
    if request.method == 'POST':
        props = get_object_or_404(Property,pk=id)
        if props.open == False:
            return redirect('Invalid Operation')
        else:
            props.open = False
            if request.user:
                props.bought_by = Account.objects.get(pk=request.user)
            props.save()
            return redirect('Front')
    else:
        return render(request,'templates/places/property_page.html')
    
def logout_(request):
    if request.user:
        try:
            logout(request)
        except:
            return render(HttpResponseBadRequest('Could Not Logout.'))
    return redirect('Front')

def invalidOperation(request):
    return HttpResponseNotFound('The Resource requested is not found')

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query','random').lower()
        props = Property.objects.filter(Q(name__icontains=query)|Q(description__icontains=query)|Q(location__icontains=query)|Q(additional_bhk__icontains=query))
        props.order_by('price')
        return render(request,'templates/places/search.html',context={'data':props})        
    else:
        return HttpResponseBadRequest('Invalid Query')

@login_required  
def confirm(request,id):
    item = get_object_or_404(Property,pk=id)
    if request.method == 'POST' and request.POST.get('full_name'):
        if item.open == False:
            return redirect('Invalid Operation')
        else:
            item.open = False
            if request.user:
                item.bought_by = Account.objects.get(pk=request.user)
            item.save()
            return redirect('Front')
    return render(request,'templates/places/confirm_buy.html',{'property':item})