
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Event, Registration


def home(request):
    events = Event.objects.all()
    return render(request, 'home.html', {'events': events})


def register(request, id):
    event = get_object_or_404(Event, id=id)

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']

        # Check duplicate registration
        already_registered = Registration.objects.filter(
            email=email,
            event=event
        ).exists()

        if already_registered:
            messages.error(
                request,
                'You have already registered for this event!'
            )
            return redirect('register', id=id)

        Registration.objects.create(
            name=name,
            email=email,
            event=event
        )

        messages.success(
            request,
            'Registration successful!'
        )

        return redirect('home')

    return render(request, 'register.html', {'event': event})


def my_registrations(request):
    registrations = []

    if request.method == 'POST':
        email = request.POST['email']
        registrations = Registration.objects.filter(email=email)

    return render(
        request,
        'my_registrations.html',
        {'registrations': registrations}
    )
