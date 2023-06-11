from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Contact,Blogs
from django.core.paginator import Paginator
# Create your views here.

def home(request):

    return render(request,'index.html')

def contact(request):
    context={'success':False}
    if request.method == "POST":
        name = request.POST['name']
        title = request.POST['title']
        descp = request.POST['desc']
        print(name,title,descp)
        ins = Contact(Name = name, title = title, descp = descp)
        ins.save()
        context={"success":True}

    return render(request,'contact.html',context)

def blogposts(request,slug):
    blogs = Blogs.objects.filter(slug=slug).first()
    context = {'blog':blogs}
    return render(request,'blogposts.html',context)

def blogs(request):
    blogs = Blogs.objects.all()
    paginator = Paginator(blogs,3)
    page = request.GET.get('page')
    pageno = paginator.get_page(page)
    print(pageno)
    context={'blogs':blogs,'pageno':pageno}
    return render(request,'blogs.html',context)