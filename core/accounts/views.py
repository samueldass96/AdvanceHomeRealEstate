from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import *
from .forms import CreateUserForm

def landingPage(request):
    #Update this with HTML page from Saikiran and Niha
    return render(request, 'accounts/homepage.html')

def aboutUs(request):
    return render(request,'accounts/AboutUs.html')

def searchListings(request):
    return render(request,'accounts/searchlistings.html')

def omahaEvents(request):
    return render(request,'accounts/omahaevents.html')

def visitorDetails(request):
    return render(request,'accounts/visitordetails.html')

def confirmationMessage(request):
    return render(request, 'accounts/confirmationmessage.html')

def filteredlistings(request):
    return render(request, 'accounts/filteredlistings.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('accounts:login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('accounts:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('accounts:home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('accounts:login')


@login_required(login_url='accounts:login')
def home(request):
    context = {}
    # return render(request, 'accounts/dashboard.html', context)
    return HttpResponseRedirect(reverse('admin:index'))
def listing_list(request):
    listings = Listing.isVisible.all()
    return render(request,
                  'accounts/listing/list.html',
                  {'listings': listings})

# Might need to change second input variable from 'id' to 'address' if doesn't work
def listing_detail(request, id):
    listing = get_object_or_404(Listing, id=id)
    return render(request,
                  'accounts/listing/detail.html',
                  {'listing': listing})
