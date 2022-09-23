from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.html import escape # Esto para evitar code injection en las URL
from django.views import View # Esto para herencias
from django import forms
from django.db.models import F
from .forms import Registration, MvpKill
from django.urls import reverse # Para obtener url by reversing
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Kills
import html
import json
import pandas as pd
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .owner import OwnerCreateView, OwnerUpdateView, OwnerDetailView
# Create your views here.

def index(request):
    return HttpResponse('Hola ke ase, kuentame lo k ase')   #Esto me lo devuelve si añado a la url /RagnarokDatabase

# ------------------ FORMS ------------------- #

def register(request):

    if request.method == 'POST':
        form = Registration(request.POST)
        # check whether it's valid:
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful")
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            return render(request, 'RagnarokDatabase/registrado.html', {'form': form.data}) # Form.data envía los datos SIN los campos, usando render.
            #return redirect('register')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = Registration()

    return render(request, 'RagnarokDatabase/Registro.html', {'form':form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("database")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")

    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form":form})

def mvp_database(request):
    try:
        if request.method == "POST":

            form = MvpKill(request.POST)

            if form.is_valid():

                names_list = []
                listmvp = pd.read_csv('RagnarokDatabase/static/Lista MVP.csv')
                for row in listmvp.itertuples():
                    names_list.append(row)

                if "check" in request.POST:
                    mvp = int(form.cleaned_data.get('name'))
                    mvp = names_list[mvp][1] #gets MVP name
                    owner = request.user
                    monster = Kills.objects.get(owner=owner, name=mvp)
                    if mvp == 'All': # For now "deprecated"
                        list = Kills.objects.all()
                        total_amount = 0
                        for mvp in list:
                            total_amount += mvp.quantity
                        show_amount = True
                        form = MvpKill()
                        return render(request,'RagnarokDatabase/mvpkills.html', context={'nombre':mvp,'num_kills':[total_amount], 'amount':show_amount, 'mvp_kills':form})
                    else:
                        show_amount = True
                        form = MvpKill()
                        
                        return render(request,'RagnarokDatabase/mvpkills.html', context={'nombre':mvp,'num_kills':[monster.quantity], 'amount':show_amount, 'mvp_kills':form})
                elif "All" in request.POST:
                    
                    list = Kills.objects.all()
                    total_amount = 0
                    for mvp in list:
                        total_amount += mvp.quantity
                    show_amount = True
                    form = MvpKill()
                    return render(request,'RagnarokDatabase/mvpkills.html', context={'nombre':mvp,'num_kills':[total_amount], 'amount':show_amount, 'mvp_kills':form})
                    
                    
                else:
                    mvp = int(form.cleaned_data.get('name'))
                    mvp = names_list[mvp][1]
                    quantity = form.cleaned_data.get('quantity')
                    obj, created= Kills.objects.update_or_create(
                        name=mvp, owner=request.user)
                    obj.quantity += quantity
                    #obj.owner= request.user.username
                    obj.save()
                    form = MvpKill()
                    return render(request,'RagnarokDatabase/mvpkills.html', context={'mvp_kills':form})
        else:

            form = MvpKill()
            context = {"mvp_kills": form}
            return render(request, 'RagnarokDatabase/mvpkills.html', context)
    except:
        form = MvpKill()
        no_mvps = True
        return render(request, 'RagnarokDatabase/mvpkills.html', context={'nomvp':no_mvps, 'mvp_kills':form})

    form = MvpKill()
    context = {"mvp_kills": form}
    return render(request, 'RagnarokDatabase/mvpkills.html', context)

# Owner views

class KillView(OwnerCreateView):
    model = Kills
    fields = ['name', 'quantity']

class KillViewUpdate(OwnerUpdateView):
    model = Kills
    fields = ['name', 'quantity']

class KillDetaiLView(OwnerDetailView):
    model = Kills
