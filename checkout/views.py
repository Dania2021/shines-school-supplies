from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There' nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51MonKeKTnlnHcYFQ4eMcfDlEkXlWoSrnhRKpIoMIS5pcGqbTArc42Kj97NagOqTLWlKMMVq62eTfge2J2of5Bo0F00rdu9C23A',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)