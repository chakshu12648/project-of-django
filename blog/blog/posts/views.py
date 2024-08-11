from django.shortcuts import render
from .models import Post


# Create your views here.
def index(requests):
         
         posts = Post.objects.all()
         return render(requests,'index.html',{'posts':posts})



def post(requests,pk):
        posts=Post.objects.get(id=pk)
        return render(requests,'posts.html',{'posts':posts})
     
   

