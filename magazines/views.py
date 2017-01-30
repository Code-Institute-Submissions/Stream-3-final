from django.shortcuts import render
from .models import Magazine
from accounts.models import User
from django.contrib.auth.decorators import login_required

@login_required
def all_magazines(request):
    magazines = Magazine.objects.all()
    args = {'magazines': magazines}
    return render(request, 'magazines.html', args)
