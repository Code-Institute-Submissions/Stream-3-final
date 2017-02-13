from django.shortcuts import render, redirect
from django.contrib import messages, auth
from accounts.forms import UserRegistrationForm, UserLoginForm, UserResetForm, ResetPasswordForm
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.conf import settings
import datetime
import stripe
import arrow
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from models import User
from django.utils.safestring import mark_safe
from  django.core.mail import EmailMessage

stripe.api_key = settings.STRIPE_SECRET

def register(request):
    domain = request.META.get('HTTP_HOST')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        subemail = request.POST.get('email')
        userExists = User.objects.filter(email=subemail)
        #print "userExists:",userExists
        if userExists:
            import hashlib
            hashemail = hashlib.sha256("jatest" + subemail)
            hexemail = hashemail.hexdigest()
            if domain == "127.0.0.1:8000":
                resetlink = "http://127.0.0.1:8000/resetuser?email=" + subemail + "&email2=" + hexemail
                loginlink = "http://127.0.0.1:8000/login/"
            else:
                resetlink = "http://johnarnold-stream3.herokuapp.com/resetuser?email=" + subemail+ "&email2=" + hexemail
                loginlink = "http://johnarnold-stream3.herokuapp.com/login/"
            messages.error(request, mark_safe("Your email address already exists, you already have an account.  Please <a href='" + loginlink + "'>Log in</a>.  If you have forgotten your password, <a href='" + resetlink + "' title='Click Here to Reset Your Password'>Reset You Password</a>."))
        else:
            if form.is_valid():
                try:
                    #customer = stripe.Charge.create(amount=499, currency='GBP', description=form.cleaned_data['email'], card=form.cleaned_data['stripe_id'],)
                    customer = stripe.Customer.create(email=form.cleaned_data['email'], card=form.cleaned_data['stripe_id'], plan='we_are_social_monthly',)
                    print "customer:",customer
                except stripe.error.CardError, e:
                    messages.error(request, 'Your card was declined!')
                if customer:
                #if customer.paid:
                    user = form.save()
                    #user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password1'))
                    user.stripe_id = customer.id#customer.stripe_id
                    user.subscription_end = arrow.now().replace(days=+31).datetime
                    user.save()
                    if user:
                        user = auth.authenticate(email=subemail, password='password', allownopassword=True)
                        auth.login(request, user)
                        auth.login(request, user)
                        messages.success(request, "You have successfully registered")
                        return redirect(reverse('profile'))
                    else:
                        messages.error(request, "Unable to log you in")
                else:
                    messages.error(request, "Unable to take payment with this card")
    else:
        today = datetime.date.today()
        form = UserRegistrationForm()

    args = {'form': form, 'publishable': settings.STRIPE_PUBLISHABLE}
    args.update(csrf(request))
    return render(request, 'register.html', args)
@login_required(login_url='/login/')
def cancel_subscription(request):
    print "test", request.user, request.user.id, request.user.stripe_id
    try:
        customer = stripe.Customer.retrieve(request.user.stripe_id)
        customer.cancel_subscription(at_period_end=True)
    except Exception, e:
        messages.error(request, e)
    return redirect('profile')

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = auth.authenticate(email=request.POST.get('email'), password=request.POST.get('password'), allownopassword=False)

            if user is not None:
                auth.login(request, user)
                messages.error(request, "You have successfully logged in")
                #return redirect(reverse('profile'))
            else:
                subemail=request.POST.get('email')
                userExists = User.objects.filter(email=subemail)

                import hashlib
                hashemail = hashlib.sha256("jatest" + subemail)
                hexemail = hashemail.hexdigest()

                if userExists:
                    domain = request.META.get('HTTP_HOST')
                    if domain == "127.0.0.1:8000":
                        resetlink = "http://127.0.0.1:8000/resetuser?email=" + subemail + "&email2=" + hexemail
                        loginlink = "http://127.0.0.1:8000/login/"
                    else:
                        resetlink = "http://johnarnold-stream3.herokuapp.com/resetuser?email=" + subemail + "&email2=" + hexemail
                        loginlink = "http://johnarnold-stream3.herokuapp.com/login/"
                    messages.error(request, mark_safe(
                        "Your email is recognised, but your password is incorrect.  Please try again.  If you have forgotten your password, <a href='" + resetlink + "' title='Click Here to Reset Your Password'>Reset You Password</a>."))
                else:
                    messages.error(request, "User Not Recognised")
    else:
        form = UserLoginForm()
    args = {'form': form}
    return render(request, 'login.html', args)

def logout(request):
    auth.logout(request)
    messages.success(request, 'You have logged out')
    return redirect(reverse('index'))

def subscriptions_webhook(request):
    event_json = json.loads(request.body)
    try:
        cust = event_json['object']['customer']
        paid = event_json['object']['paid']
        user = User.objects.get(stripe_id=cust)

        if user and paid:
            user.subscription_end = arrow.now().replace(weeks=+4).datetime

    except stripe.InvalidRequestError, e:
        return HttpResponse(status=404)
    return HttpResponse(status=200)

def reset_user(request):
    domain = request.META.get('HTTP_HOST')
    if request.method == "POST":
        form = UserResetForm(request.POST)
        emailsent = True
        email1 = request.POST["username"]
        hashemail = request.POST["hashemail"]
        import hashlib
        hashemail1 = hashlib.sha256("jatest" + email1)
        hexemail1 = hashemail1.hexdigest()
        if hashemail == hexemail1:
            valid = True
        else:
            valid = False

        if valid:
            if domain == "127.0.0.1:8000":
                resetlink = "http://127.0.0.1:8000/reset?email=" + email1 + "&email2=" + hexemail1
            else:
                resetlink = "http://catkin-art-1.herokuapp.com/reset?email=" + email1 + "&email2=" + hexemail1
            subject = "We Are Social - Reset User Account"
            resetlink = "<a href='" + resetlink + "'>" + resetlink + "</a>"
            reset_message = "<html><body><p>We are social, reset user account.</p> <p>Please click the following link to reset your password and activate your user account:</p><p>" + resetlink + "</p></body></html>"

            email = EmailMessage(
                subject,
                reset_message,
                'sender smtp gmail' + '<catkin.order@gmail.com>',
                [email1, 'arnold-j83@sky.com'],
                headers={'Reply-To': 'nicky.atkin@gmail.com'}
            )
            email.content_subtype = 'html'
            email.send()

            emailsent = True
            messages.success(request,
                       "Thank you, an email has been sent to you containing details of how you can reset your account password and activate your account.")

    else:
        email = request.GET["email"]
        hashemail = request.GET["email2"]
        import hashlib
        hashemail1 = hashlib.sha256("jatest" + email)
        hexemail1 = hashemail1.hexdigest()
        if hashemail == hexemail1:
            valid = True
        else:
            valid = False

        if valid:
            form = UserResetForm(initial={'username': email, 'hashemail': hexemail1})
            messages.success(request, "Please Click the Send Reset Email Button Below")
            emailsent = False
        else:
            form = UserResetForm()
            messages.error(request, "An Error Has Occured, please go back and click the link again")
            emailsent = True
    args = {'form': form, 'emailsent': emailsent}
    args.update(csrf(request))
    return render(request, 'reset1.html', args)

def reset(request):
    domain = request.META.get('HTTP_HOST')
    if request.method == "POST":
        email1 = request.POST.get('username')
        p = User.objects.get(username=email1)
        password = p.password
        form = ResetPasswordForm(request.POST, instance=p)
        password = request.POST.get('password2')
        reset = False
        if form.is_valid():
            reset = True
            form.save()
            form.add_error(None, "Thank you, your password has been changed and your account has been activated :)")
            user = auth.authenticate(email=email1, password=password, allownopassword=True)
            auth.login(request, user)
    else:
        reset = False
        email1 = request.GET['email']
        form = ResetPasswordForm(initial={'username': email1})
    args = {'form': form, 'reset': reset}
    args.update(csrf(request))
    return render(request, 'resetuser.html', args)