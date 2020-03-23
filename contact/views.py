from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import contactForm



def contact(request):
    title = 'Get into Touch'
    form = contactForm(request.POST or None)
    confirm_message = None
    
    if form.is_valid():
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'MESSAGE FROM GRANTHA TOURS AND TRAVELLS'
        message = '%s %s' %(name, comment)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail( subject, comment, emailFrom, emailTo, fail_silently=True)
        title = "Thanks for the message."
        confirm_message = "Thanks for the message, we will get right back to you."
        form = None

    context = { 'title' : title,  'form' : form,  'confirm_message' : confirm_message }
    template = 'contact.html'
    return render(request, template, context)