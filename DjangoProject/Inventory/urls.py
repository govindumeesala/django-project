from django.urls import path

from .views import *

urlpatterns=[
    path('home/', HomePage),
    path('login/', LoginPage),
    path('contact/', ContactPage),
    path('service/', ServicePage),
    path('interns/add/',Interns_add_page),
    path('interns/', Interns_details),
    path('interns/delete/<int:id>/', Delete_intern, name='intern_delete'),
    path('interns/update/<int:id>/', Update_intern, name='intern_update'),
]  