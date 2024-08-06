from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect



# Create your views here.
def login(request):
    # Your login view logic here
    print(request.POST)
    print(request.POST)

    if(request.method=='POST'):
       username=request.POST['username']
       password=request.POST['password']
       
       user=auth.authenticate(username=username,password=password)

       if user is not None:
          auth.login(request,user)
          return redirect('/')
       else:
          messages.info(request,'invalid credentials')
          return redirect('login')
    else:
        return render(request, 'login.html')  
       
    
def register(request):
   if request.method=='POST':
      username=request.POST['username']
   
      email=request.POST['email']
      password=request.POST['password']
      password2=request.POST['password2']
      if password==password2:
         if User.objects.filter(email=email).exists():
            messages.info(request,'Email already used')
            return redirect('register')
         elif User.objects.filter(username=username).exists():
            messages.info(request,'username already taken')
            return redirect('register')
         else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            return redirect('login') 
      else:
         messages.info(request,'not the correct password')
         return redirect('register')

   
   else:
      return render(request,'register.html')
def index(request):
   

   return  render(request,'index.html',)







