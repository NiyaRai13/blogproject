from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from myapp.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    blog=Blog.objects.all()
    return render(request, 'main/index.html', {'blog': blog})

@login_required
def addblog(request):
    errors={}
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        description = request.POST.get('description')

        if not title:
            errors['title']="Title is required"

        
        if not category:
             errors['category']="Category is required"

        if not description:
                errors['description']="Description is required"

        if not image:
                errors['image']="Image is required"
   
        if errors:
              return render (request,'main/addblog.html',{'errors':errors,'data':request.POST})
             

        Blog.objects.create(
                title=title, 
                category=category, 
                image=image,
                description=description,
                author=request.user
             
        )

        # Here you would typically save the blog post to the database
        # For example:
        # blog = Blog(title=title, image=image, category=category, description=description)
        # blog.save()

        return render(request, 'main/addblog.html', {'message': 'Blog added successfully!'})

    return render(request, 'main/addblog.html')

def blog_page(request,id):
     blog=Blog.objects.get(id=id)
     return render(request,'main/blogpage.html',{'blog':blog})

def edit_blog(request,id):
    previous_data=Blog.objects.get(id=id)
    errors={}
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        description = request.POST.get('description')

        if previous_data.author != request.user:
            title = previous_data.title
            if image  :
                 image = previous_data.image
            category = previous_data.category
            description = previous_data.description
            previous_data.save()
            
            
        
            messages.error(request, "You are not authorized to edit this blog.")
            return  redirect('blog_page', id=id)

    return render(request, 'main/editblog.html', {'message': 'Blog updated successfully!', 'blog': previous_data})

        
         
             
       

        
def delete_blog(request, id):
    blog = Blog.objects.get(id=id)
    if blog.author != request.user:
        messages.error(request, "You are not authorized to delete this blog.")
        return redirect('blog_page', id=id)

    blog.delete()
    messages.success(request, "Blog deleted successfully!")
    return redirect('index')
@login_required
def profile(request , id):
    user = get_object_or_404 (User, id=id)
    errors = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email')

        if not username:
             errors['username'] = "Username is Required."
        # elif User.objects.filter(username=username).exists():
        #      errors['username'] = "Username already exist."

        if not email:
             errors['email'] = "Email is Required."
    
        if errors:
            return render(request, 'main/userprofile.html',{'errors': errors}) 
        
        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        messages.success(request,'Profile updated successfully.')
        # return render(request,'main/profile.html', {'message':"Profile updated successfully."}) 
        return redirect('index') 
    
    return render(request, 'main/userprofile.html', {'user': user})
def change_password(request,id):
    user = get_object_or_404(User, id=id)
    errors={}
    if request.method == 'POST':
        password=request.POST.get('password')
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')

        if not request.user.check_password(password):
          errors['password']='password doesnot match with old password'
        elif not password:
            errors['password']='password is required'
        if new_password != confirm_password:
            errors['confirm_password']='password doesnnot match'
        elif not new_password:
            errors['new_password']='new pasword is required'
        if not confirm_password:
            errors['confirm_password']='confirm password is required'

        if errors:
            return render(request,'main/password.html',{'error': errors})
        try:
            request.user.set_password(new_password)
            request.user.save()
            return redirect('index')
        except Exception as e:
            errors['confirm_password']=f'Failed to reset password{e}'
            return render(request,'main/password.html',{'error':errors})
        
    return render(request,'main/password.html',{user:'user'})