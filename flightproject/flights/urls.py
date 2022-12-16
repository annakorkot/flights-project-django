from django.contrib import admin
from django.urls import path 
from .views import search_flights ,book_ticket ,TicketList


urlpatterns = [
    path('search/', search_flights ,name='search_flight.html'),
    path('book_flight/', book_ticket , name = 'book_flight.html'),
    path('my_tickets',TicketList.as_view(),name='my_tickets.html')
    
]