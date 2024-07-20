from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def recipies(request):
    if request.method=="POST":
         data=request.POST
         recepie_image=request.FILES.get('recepie_image')
         recepie_name= data.get('recepie_name')
         recepie_des= data.get('description')
         print(recepie_name)
         print(recepie_des)
         print(recepie_image)
         recipie.objects.create(
              recipie_image=recepie_image,
              recipie_description=recepie_des,
              recipie_name=recepie_name,
              
         )

         return redirect("/recepies/")
    

    queryset=recipie.objects.filter(is_approved=True)
    if request.GET.get("search"):
         queryset=queryset.filter(recipie_name__icontains=request.GET.get('search'))
         
    
    context={"recipie":queryset}
        


   
    return render(request,"recepies.html",context)

@login_required(login_url="/login")
def update_recipie(request,id):
     # print(id)
     queryset =recipie.objects.get(id=id)
     if request.method =="POST":
         data=request.POST
         recepie_image=request.FILES.get('recepie_image')
         recepie_name= data.get('recepie_name')
         recepie_des= data.get('description')
         queryset.recipie_name=recepie_name
         queryset.recipie_description=recepie_des
         if recepie_image:
              queryset.recipie_image=recepie_image
     
         queryset.save()
         return redirect('/edit-recepies')
         
     context={'recepie':queryset}
     return render(request,"update.html",context)

@login_required(login_url="/login")
def delete_recipie(request,id):
     # print(id)
     queryset =recipie.objects.get(id=id)
     queryset.delete()
     return redirect('/edit-recepies/')

@login_required(login_url="/login")
def add_recepies(request):
     if request.method=="POST":
         data=request.POST
         recepie_image=request.FILES.get('recepie_image')
         recepie_name= data.get('recepie_name')
         recepie_des= data.get('description')
         print(recepie_name)
         print(recepie_des)
         print(recepie_image)
         recipie.objects.create(
              recipie_image=recepie_image,
              recipie_description=recepie_des,
              recipie_name=recepie_name,
              
         )

         return redirect("/recepies/")    
     return render(request,"add recepie.html")

@login_required(login_url="/login")
def edit_recepies(request):
     queryset=recipie.objects.all()
     context={"recipie":queryset}
     return render(request,"edit recepies.html",context)

def login_page(request):
     if request.method=="POST":
          username=request.POST.get('username')
          password=request.POST.get('password')

          if not User.objects.filter(username = username).exists():
               messages.error(request, "invalid Username")
               return redirect("/login")
          
          user=authenticate(username=username,password=password)


          if user is None:
               messages.error(request, "invalid password")
               return redirect('/login')
          else:
               login(request,user)
               return redirect("/recepies")
     

     return render(request,"login.html")

def log_out(request):
     logout(request)
     return redirect("/login")

def register_page(request):
     if request.method=="POST":
          first_name=request.POST.get('first_name')
          last_name=request.POST.get('last_name')
          username=request.POST.get('username')
          password=request.POST.get('password')

          user=User.objects.filter(username=username)

          if user.exists():
               messages.info(request, "Username already taken")
               return redirect('/register')
          


          user= User.objects.create(
               first_name=first_name,
               last_name=last_name,
               username=username,
               password=password
          )
          user.set_password(password)
          user.save()
          messages.success(request, "Account created ")
          return redirect('/register')
          
     

     return render(request,"register.html")