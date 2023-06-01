from django.shortcuts import render


def index(request):
    """
    A view to return the index page
    """

    return render(request, 'home/index.html')


def privacy(request):
    """
    A view to the privacy page
    """

    return render(request, 'home/privacy.html')


def terms(request):
    """
    A view to the terms page
    """

    return render(request, 'home/terms.html')


def delivery(request):
    """
    A view to the delivery page
    """

    return render(request, 'home/delivery.html')
