from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse 
from .models import Blog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from .forms import createBlogForm, editBlogForm

# Home page view 
def homePage(request):
    blogs = Blog.objects.all()
    return render(request,'Blog/homePage.html',{'blogs':blogs})


# Full detail of blog
def blogDetail(request,blog_id):
    blog = get_object_or_404(Blog,id=blog_id)
    return render(request,'Blog/blogDetail.html',{'blog':blog})


# view to create blog
def createBlog(request):
    if request.method == 'POST':
        form = createBlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('homePage')
        form = createBlogForm()
        return render(request,'Blog/createBlog.html',{'form':form})
    else:
        form = createBlogForm()
        return render(request,'Blog/createBlog.html',{'form':form}) 



# view to edit blog
def editBlog(request,blog_id):
    blogU = get_object_or_404(Blog,pk=blog_id,author = request.user)    
    if request.method == 'POST':
        form = editBlogForm(request.POST,request.FILES,instance=blogU)
        if form.is_valid():
            blogU = form.save(commit=False)
            blogU.author = request.user
            blogU.save()
            return redirect('homePage')
    else:
        form = editBlogForm(instance=blogU)
    return render(request,'Blog/editBlog.html',{'form':form})

# delete blog
def deleteBlog(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'Blog/deleteBlog.html',{'blog':blog})


def confirmDeleteBlog(request,blog_id):
    object_to_delete = get_object_or_404(Blog,pk=blog_id)
    if object_to_delete:
        if request.user == object_to_delete.author:
            object_to_delete.delete()
            return redirect('homePage')
# login blog
@csrf_protect
def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username = username,password = password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('homePage')
            else:
                return HttpResponse("User is not active")
        else:
            return HttpResponse("Invalid credentials!")
    else:
        return render(request,'Blog/loginPage.html')


# logout view
def logoutPage(request):
    logout(request)
    return redirect('loginPage')


# register view 
@csrf_protect
def registerPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if pass1 != pass2:
            return HttpResponse('Password and confirm password are not same')
        else:
            user = User.objects.create_user(username,email,pass1)
            user.save()
            return redirect('loginPage')
    else:
        return render(request,'Blog/registerPage.html')

