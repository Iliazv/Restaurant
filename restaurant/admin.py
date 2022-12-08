from django.contrib import admin
from .models import Dish, User_Message, Wine, Reservation

#il

admin.site.register(Dish)
admin.site.register(Wine)
admin.site.register(User_Message)
admin.site.register(Reservation)