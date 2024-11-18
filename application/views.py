from django.shortcuts import render, redirect
from .forms import AppointmentForm, ContactForm

def index(request):
    # Initialize both forms
    appointment_form = AppointmentForm()
    contact_form = ContactForm()

    if request.method == 'POST':
        if 'appointment_submit' in request.POST:  # Check which form was submitted
            appointment_form = AppointmentForm(request.POST)
            if appointment_form.is_valid():
                appointment_form.save()
                return redirect('index')  # Redirect after saving appointment form to avoid resubmission issues
        elif 'contact_submit' in request.POST:
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                contact_form.save()
                return redirect('index')  # Redirect after saving contact form to avoid resubmission issues

    context = {
        'appointment_form': appointment_form,
        'contact_form': contact_form,
    }

    return render(request, 'index.html', context)
