# from django.http import HttpResponse
# from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# from django.contrib.auth.decorators import login_required

# import pdb
from .forms import CreateUserForm

# Create your views here.

def account(request):
    # password = request.POST['password']
    # print(request)
    # pdb.set_trace()
    # username = request.POST["username"]
    # password = request.POST["password"]
    # user = authenticate(request, username=username, password=password)
    #
    # if user is not None:
    #     login(request, user)
    #     messages.add_message(request, messages.SUCCESS, "Vous êtes connecté !")
    # else:
    #     messages.add_message(
    #         request, messages.ERROR, "Les champs renseignés sont invalides."
    #     )

    # return redirect("home")

    return render(request, 'user/account.html')

def essais(request):
    username = request.POST["username"]
    return render(request, 'user/account.html')

def index(request):
    return render(request, 'user/index.html')

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('welcome')
        else:
            messages.info(request, 'Nom utilisateur ou mot de passe incorrect')
            # return render(request, 'user/login.html', context)
    # form = UserCreationForm()
    context = {}
    return render(request, 'user/login_page.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def register_page(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Le compte à été créé pour' + user)
            # return redirect('login_page')
    context = {'form': form}
    return render(request, 'user/register_page.html', context)
