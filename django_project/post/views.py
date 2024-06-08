from django.shortcuts import render, redirect
from django.contrib import messages
from .form import CreatePostForm, UpdatePostForm
from .models import Post


# Create post
def create_post(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Sorry, you are not create a post except you logged in!")
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreatePostForm(request.POST)
            if form.is_valid():
                var = form.save(commit=False)
                var.created_by = request.user
                var.save()
                if var.is_published:
                    messages.info(request,"New post created")
                    return redirect('all-created-posts')
                else:
                    messages.warning(request,"New post created! But not Published")
                    return redirect('all-created-posts')              
            else:
                messages.warning(request,'Something went wrong')
                return redirect('create-post')
        else:
            form = CreatePostForm()
        context = {'form': form}
        return render(request,'post/create_post.html', context)
        


# view post details
def post_details(request, pk):
    post = Post.objects.get(pk=pk)
    context = {'post': post}
    return render(request,'post/post_details.html',context)
    

# update post 
def update_post(request, pk):
    if not request.user.is_authenticated:
        messages.warning(request,"Sorry, you are not create a post except you logged in!")
    else:
        post = Post.objects.get(pk=pk)
        if request.user == post.created_by:
            if request.method == 'POST':
                form = UpdatePostForm(request.POST, instance=post)
                if form.is_valid():
                    form.save()
                    messages.info(request,"Post has been updated")
                    return redirect('all-created-posts')
                else:
                    messages.warning(request,'Something went wrong')
                    # return redirect('') 
            else:
                form = UpdatePostForm(instance=post)
            context = {'form': form, 'post': post}
            return render(request,'post/update_post.html', context)
        else:
            messages.warning(request,"Sorry, you are have permission to change this!")
            return redirect('all-created-posts')


# delete post
def delete_post(request, pk):
    if not request.user.is_authenticated:
        messages.warning(request,"Sorry, you are not delete a post except you logged in!")
    else:
        post = Post.objects.get(pk=pk)
        if request.user == post.created_by:
            post.delete()
            return redirect('home')
        else:
            messages.warning(request,"Sorry, you are have permission to change this!")
            return redirect('all-created-post')


# see all post that they have created
def all_created_posts(request):
    post = Post.objects.filter(created_by=request.user)
    context = {'post': post}
    return render(request,'post/all_created_posts.html', context)


# visitors can view all posts
def all_posts(request):
    post = Post.objects.filter(is_published=True)
    context = {'post': post}
    return render(request,'post/all_posts.html', context)