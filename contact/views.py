from django.shortcuts import render, redirect
from .forms import ContactUsForm
from profiles.models import UserProfile

from django.contrib import messages


def contact(request):

    if request.method == 'POST':
        contact_form = ContactUsForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'Message sent successfully.')
            return render(request, 'contact/contact_success.html')
        else:
            messages.error(request, 'There was an error sending your message. \
            Please ensure all fields are valid.')
            return redirect('contact')

    else:
        if request.user.is_authenticated:
            try:
                user = UserProfile.objects.get(user=request.user)
                contact_form = ContactUsForm(initial={
                    'contact_name': user.default_full_name,
                    'contact_email': user.user.email,
                    'contact_phone_number': user.default_phone_number,
                })
            except UserProfile.DoesNotExist:
                contact_form = ContactUsForm()
        else:
            contact_form = ContactUsForm()

    template = 'contact/contact.html'
    context = {
        'form': contact_form,
    }

    return render(request, template, context)
