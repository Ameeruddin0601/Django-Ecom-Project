from django.shortcuts import redirect, render
from accounts.forms import RegistrationForm
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from accounts.models import Account
def register(request):
    form = RegistrationForm()
    if request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, email=email, userName=username, password=password)
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration Successful')
            return redirect('register')
        else:
            pass
    context = {
		'form': form,
	}
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, "invalid credentials")
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')
