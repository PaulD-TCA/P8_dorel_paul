from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Product, Backup
from django.contrib.auth.models import User
from .forms import NameForm
# from django import forms

def home(request):

    template = loader.get_template('search_and_sub/home.html')
    context = {}
    # return HttpResponse("Hello, search.")
    return HttpResponse(template.render(context, request))

def search(request):
    return HttpResponse("Hello, search.")

def food_page(request, id):#, product_id):
    template = loader.get_template('search_and_sub/food_page.html')
    print(id)
    food_details = Product.objects.filter(id=id)
    print(food_details)
    context = {'food_details':food_details,}
    return HttpResponse(template.render(context, request))

def save_page(request, id):#, product_id):
    template = loader.get_template('search_and_sub/save_page.html')
    # print(id)
    food_details = Product.objects.filter(id=id)
    # print(food_details)
    current_user = request.user.id
    print(current_user)
    # print(User.objects.get(id=request.user))
    food_to_save = Backup(p_id_id=id, u_id_id=current_user)
    food_to_save.save()
    context = {'food_details':food_details,}
    return HttpResponse(template.render(context, request))


# def food_page(request):#, product_id):
#     template = loader.get_template('search_and_sub/food_page.html')
#     context = {}
    # return HttpResponse("Hello, search.")
    # return HttpResponse(template.render(context, request))

def results(request):
    print("results")
    if request.method == 'POST':
        print("post")

        form = NameForm(request.POST)
        print(form)
        if form.is_valid():
            user_query = form.cleaned_data['your_name']
            # foods = Product.objects.filter(p_name=user_query)
            print(user_query)
            foods = Product.objects.all()
            template = loader.get_template('search_and_sub/results_page.html')
            context = {
    #         # 'foodmore':foodmore,
    #
            'foods':foods,
            }
    #
            return HttpResponse(template.render(context, request))

    template = loader.get_template('search_and_sub/results_page.html')
    context = {}
    return HttpResponse(template.render(context, request))

def my_favourites(request):
    # if request.user.is_authenticated:
    current_user = request.user.id
    print(current_user)
    favourites_list = Product.objects.filter(backup__u_id_id=current_user)
    # favourites_list = Backup.objects.select_related('p_id')#.get(u_id_id=current_user)#.select_related("p_id")#("Product")
    # favourites_list = Backup.objects.filter(u_id_id=current_user)#.select_related("p_id")#("Product")
    # favorites_products = favourites_list.Product

    template = loader.get_template('search_and_sub/my_favourites_page.html')
    context = {'favourites_list':favourites_list}
    # return HttpResponse("Hello, favourites.")
    return HttpResponse(template.render(context, request))
