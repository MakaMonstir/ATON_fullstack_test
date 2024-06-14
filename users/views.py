from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import UserLoginForm

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('clients')
    else:
        form = UserLoginForm()
    return render(request, 'myapp/login.html', {'form': form})

@login_required
def clients_view(request):
    clients = Client.objects.filter(responsible_person=request.user)
    return render(request, 'myapp/clients.html', {'clients': clients})

@login_required
def update_status(request, client_id, status):
    client = Client.objects.get(id=client_id)
    client.status = status
    client.save()
    return redirect('clients')
