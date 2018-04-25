from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from home.forms import RegisterForm
from django.contrib.auth.decorators import login_required

from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the Home index.")


def base(request):
    return render(request, 'base1.html')


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username = username, password = raw_password)
#             login(request, user)
#         return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})
#

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
        return redirect(base)
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form': form})


# def sendSimpleEmail(request):
#     res = send_mail("send from django framework",
#                     "emails body here",
#                     "kapil128@hotmail.com",
#                     ["kapilmeena8959@gmail.com", "kapil128@hotmail.com"]
#                     )
#     return HttpResponse('%s'%res)

# @login_required(login_url='/accounts/login/')
@login_required
def sendSimpleEmail(request):
    res = EmailMessage("send from django framework using EmailMessage()",
                    "emails body here new with disrted cleared again backend",
                    "kapil128@hotmail.com",
                    ["kapilmeena8959@gmail.com", "kapil128@hotmail.com"]
                    )

    return HttpResponse('%s'%res.send())
