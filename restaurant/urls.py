from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.show_menu, name="show_menu"),
    path('menu_list/', views.show_list, name="show_food"),
    path('menu_list/<int:dish_category>', views.show_list, name="show_food"),
    path('menu_wine/', views.show_wine, name="show_wine"),
     path('menu_wine/<int:wine_category>', views.show_wine, name="show_wine"),
    path('show_reservation/', views.show_reservation, name="show_reservation"),
    path('show_searched_food/', views.show_searched_food, name="show_searched_food"),
    path('show_searched_wine/', views.show_searched_wine, name="show_searched_wine"),
    path('add_reservation/', views.add_reservation, name="add_reservation"),
    path('add_message/', views.add_message, name="add_message"),
    path('add_message/', views.add_message, name="add_message"),
    path('<str:anch>/', views.show_menu, name="show_menu"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)