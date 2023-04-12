from django.shortcuts import render
from .models import Food, BookTable, Table, Response, Event, Category


def home(request):
    return render(request, 'home.html')


def menu_category(request, id):
    ...
    return render(request, 'menu.html', context)


def menu(request):
    ...
    return render(request, 'menu.html', context)


def booktable(request):
    ...
    return render(request, 'booktable.html', {'tables': tables})


def contact(request):
    ...
    return render(request, 'contact.html')


def event(request):
    ...
    return render(request, 'event.html', {'events': events})