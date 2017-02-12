from django.shortcuts import render
from .forms import contactForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ContactSerializer
from .models import contact_data
from django.template.context_processors import csrf
from  django.core.mail import send_mail, EmailMessage

class ContactView(APIView):
    serializer_class = ContactSerializer

    def get(self, request):

        contacts = contact_data.objects.order_by('-enquiry_date')
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

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
            catkin_subject = "Enquiry from Catkin Art Website"
            catkin_message = "Enquiry from: " + name + " \n\n Email: " + email + " \n\n Phone: " + phone + " \n\n Enquiry: " + enquiry
            email = EmailMessage(
                catkin_subject,
                catkin_message,
                'sender smtp gmail' + '<catkin.order@gmail.com>',
                ['arnold-j83@sky.com'],
                headers={'Reply-To': 'nicky.atkin@gmail.com'}
            )
            email.send()

    else:
        form = contactForm()

    args = {'form':form}
    args.update(csrf(request))
    return render(request, 'contact_form.html', args)
