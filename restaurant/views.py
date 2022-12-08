from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from restaurant.models import Dish, Wine, User_Message, Reservation

def show_menu(request):
    content = {}
    template = loader.get_template('restaurant/menu_page.html')
    return HttpResponse(template.render(content, request))   

def show_list(request, dish_category=0):
    food = Dish.objects.all()
    content = {'food': food, 'dish_category': dish_category}
    template = loader.get_template('restaurant/list_page.html')
    return HttpResponse(template.render(content, request))   

def show_wine(request, wine_category=0):
    wines = Wine.objects.all()
    content = {'wines': wines, 'wine_category': wine_category}
    template = loader.get_template('restaurant/wine_page.html')
    return HttpResponse(template.render(content, request))   

def show_reservation(request):
    content = {}
    template = loader.get_template('restaurant/reservation.html')
    return HttpResponse(template.render(content, request))    

def add_reservation(request):
    FIO = request.POST.get('FIO')
    telephone = request.POST.get('telephone')
    email = request.POST.get('email')
    guests = request.POST.get('guests')
    time = request.POST.get('time')
    comment = request.POST.get('comment')
    reservation = Reservation(FIO=FIO, phone=telephone, email=email, guests=guests, time=time, comment=comment)
    reservation.save()

    content = {}
    template = loader.get_template('restaurant/reservation.html')
    return HttpResponse(template.render(content, request))    

def add_message(request, anch='0'):
    name = request.POST.get('name')
    phone = request.POST.get('telephone')
    comment = request.POST.get('message')

    message = User_Message(name=name, phone=phone, message=comment)
    try: 
        message.save()
    except:
        anch = '1'
    
    content = {'anch': anch}
    template = loader.get_template('restaurant/menu_page.html')
    return HttpResponse(template.render(content, request))
    
def show_searched_food(request):
    input = request.POST.get('search_box')
    input = input.capitalize()
    searched_food = Dish.objects.filter(Q(name__istartswith=input))

    content = {"searched_food": searched_food}
    template = loader.get_template('restaurant/list_page.html')
    return HttpResponse(template.render(content, request))

def show_searched_wine(request):
    input = request.POST.get('search_box')
    input = input.capitalize()
    searched_wine = Wine.objects.filter(Q(name__istartswith=input))

    content = {"searched_wine": searched_wine}
    template = loader.get_template('restaurant/wine_page.html')
    return HttpResponse(template.render(content, request))