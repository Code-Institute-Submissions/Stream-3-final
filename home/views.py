from django.shortcuts import render
from blog.models import Post
from threads.models import Subject, Thread
from django.utils import timezone

def get_index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0]
    forum_subjects = Subject.objects.all()[:2];
    print "forum_subject:",forum_subjects
    args = {'posts': posts, 'forum_subjects': forum_subjects}
    return render(request, 'index.html', args)
