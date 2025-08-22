from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def index(request):
    return render(request, 'portfolio_app/index.html')

def index(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject=f"Portfolio Contact Form - {name}",
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['muppuraj11@gmail.com'],  # change to your email
                fail_silently=False,
            )
            success = True
    else:
        form = ContactForm()

    return render(request, 'portfolio_app/index.html', {'form': form, 'success': success})



def success_page(request):
    name = request.GET.get('name', 'User')
    return render(request, 'portfolio_app/success.html', {'name': name})