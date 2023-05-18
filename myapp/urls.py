from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_data/', add_data, name='add_data'),
    path('del_data/', del_data, name='del_data'),

]