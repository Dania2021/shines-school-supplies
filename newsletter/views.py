from django.http import HttpResponseRedirect

from django.contrib import messages
from .models import Subscriber
from .forms import SubscriberForm


def add_subscriber(request):
    """Add email to the subscriber list"""

    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)

        if Subscriber.objects.filter(email=instance.email).exists():
            messages.error(
                request,
                f"{instance.email} already exists. Please check your email \
                    and try again."
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            instance.save()
            messages.success(
                request,
                f"{instance.email} has been successfully added \
                    to our mailing list"
            )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
