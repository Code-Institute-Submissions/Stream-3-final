from django.shortcuts import render
from .forms import contactForm
from django.template.context_processors import csrf
from  django.core.mail import send_mail, EmailMessage
from django.contrib import messages

def contact_form1(request):
    name = request.POST.get('name')
    print "name1:", name
    if request.method == "POST":
        form = contactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            enquiry = request.POST.get('enquiry')
            contact = form.save(False)
            contact.save()
            email_subject = "Enquiry from We Are Social"
            email_message = "Enquiry from: " + name + " \n\n Email: " + email + " \n\n Phone: " + phone + " \n\n Enquiry: " + enquiry
            email = EmailMessage(
                email_subject,
                email_message,
                'sender smtp gmail' + '<catkin.order@gmail.com>',
                ['arnold-j83@sky.com'],
                headers={'Reply-To': 'test.test@gmail.com'}
            )
            email.send()
            args = {'form': form, 'submitted': 'Yes'}
            messages.success(request, "Your message has been sent to us, we aim to reply within 24 hours")
        else:
            args = {'form': form, 'submitted': 'No'}
            messages.error(request, "Your message has not been sent, there is an error, please check everything and try again!")


    else:
        form = contactForm()
        args = {'form': form, 'submitted': False}

    args.update(csrf(request))
    return render(request, 'contact_form.html', args)
