from django.shortcuts import render
from blog.models import Post
from django.utils import timezone

def get_index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0]
    args = {'posts': posts}
    return render(request, 'index.html', args)
