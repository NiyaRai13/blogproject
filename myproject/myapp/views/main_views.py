from django.shortcuts import render
from myapp.models import Blog
from django.contrib.auth.decorators import login_required


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
    blog=Blog.objects.get(id=id)
    errors={}
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        description = request.POST.get('description')

        if blog.author != request.user:
            return render(request, 'main/editblog.html', {'error': 'You are not authorized to edit this blog.'})

        if not title:
            errors['title']="Title is required"

        
        if not category:
             errors['category']="Category is required"

        if not description:
                errors['description']="Description is required"

        if not image:
                errors['image']="Image is required"
   
        if errors:
              return render (request,'main/editblog.html',{'errors':errors,'data':request.POST,'blog':blog})
         
             
        blog.title=title
        blog.category=category
        blog.image=image
        blog.description=description
        blog.save()

        return render(request, 'main/editblog.html', {'message': 'Blog updated successfully!','blog':blog})

    return render(request, 'main/editblog.html',{'blog':blog})

def delete_blog(request,id):
    blog=Blog.objects.get(id=id)
    if request.method == 'POST':
        blog.delete()
        return render(request, 'main/index.html', {'message': 'Blog deleted successfully!'})
    return render(request, 'main/deleteblog.html', {'blog': blog})