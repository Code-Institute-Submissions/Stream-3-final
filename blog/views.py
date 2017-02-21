from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    print posts
    args = {'posts': posts}
    return render(request, 'blogposts.html', args)

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    post.views +=1
    post.save()
    args={'post': post}
    return render(request, 'postdetail.html', args)

@login_required
def new_post(request):
    if request.method == 'POST':
        form=BlogPostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()
        args = {'form': form}
    return render(request, 'blogpostform.html', args)

def edit_post(request, id):
    post = get_object_or_404(Post, pk=id)
    print "post:",post
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
        args = {'form': form}
    return render(request, 'blogpostform.html', args)
