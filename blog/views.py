from django.shortcuts import render
from .models import Post

# this function takes a request and return http response
# we have to match it with Url pattern to this view function
def home(request):
    context ={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

def about(request):
    return render(request, 'blog/about.html',{'title':'about'})