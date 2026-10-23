from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def balance(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        amount=request.POST.get('amount', 0)
        request.user.userprofile.userBalance = float(request.user.userprofile.userBalance) + float(amount)
        request.user.userprofile.save()
        messages.success(request, 'Funds added successfully.')
    return render(request, 'users/balance.html')
