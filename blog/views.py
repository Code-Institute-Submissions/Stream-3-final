from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

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
