from .forms import SubscriberForm


def render_subscribe_form(request):
    """ Render newsletter form across all pages """

    subscriber_form = SubscriberForm()

    context = {
        'subscriber_form': subscriber_form,
    }

    return context
