from django.contrib import admin
from django.urls import path
from ReservasApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index,name='home'),
    path('reservasList/', reservasList, name='reservasList'),

]