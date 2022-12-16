from django.shortcuts import render ,redirect
from datetime import datetime
from .models import Flight ,Customer ,Ticket
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

def search_flights(request):
    all_flights = Flight.objects.all()
    all_flights=all_flights.filter(remaning_tickets__gte=1)
   
    
    country_from = request.GET.get('country_from')
    country_to = request.GET.get('country_to')
    date_start = request.GET.get('date_start')
    date_end = request.GET.get('date_end')
    number_of_tickets = request.GET.get('number_of_tickets')
    

    def check_value(value):
        if value != "" and value is not None:
            return value

    
    if number_of_tickets is not None :
        number_of_tickets=int(number_of_tickets)
        all_flights = all_flights.filter(remaning_tickets__gte=number_of_tickets)

    if check_value(country_from):
            all_flights = all_flights.filter(origin_country__name__icontains = country_from)

    if check_value(country_to):
            all_flights = all_flights.filter(destination_country__name__icontains = country_to)
            
    if check_value(date_start):
            date_start = datetime.strptime(date_start, "%Y-%m-%d")
            all_flights=all_flights.filter(departure_time__gte = date_start)

    if check_value(date_end):
            date_end = datetime.strptime(date_end , "%Y-%m-%d")
            all_flights = all_flights.filter(landing_time__lte = date_end)



    context ={
            'queryset': all_flights
        }

    Paginator(all_flights, 5)

    return render(request ,'search_flight.html',context)

@login_required
def book_ticket(request):
       
    if request.POST.get('flight_id') is not None:
        flight_id=int(request.POST.get('flight_id'))
        flight =Flight.objects.filter(id__exact=flight_id).first()
        
    if request.POST.get('create_ticket')=='true' and flight.remaning_tickets > 0: #if customer clicks "book this flight"- button, it will save the ticket to database
        customer = Customer.objects.filter(user__id__exact = request.user.id).first()
    
        if customer is None:
            messages.error(request,"Please update profile to book flight")
            return redirect("update_profile")

        ticket = Ticket.objects.create(flight=flight, customer=customer)
        tickets_left=flight.remaning_tickets - 1
        flight.remaning_tickets = tickets_left
        flight.save()
    
        messages.success(request,f'flight from:{flight.origin_country} to:{flight.destination_country} booked')
    
        return redirect("homepage")
   
    return render(request,'book_flight.html',{'flight':flight})

class TicketList(LoginRequiredMixin, ListView):

    model = Ticket
    context_object_name = 'tickets'
    template_name = 'my_tickets.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):

        user = self.request.user
        customer = Customer.objects.filter(user__id__exact =user.id).first()
        all_tickets = super(TicketList, self).get_queryset(*args, **kwargs)

        user_tickets = all_tickets.filter(customer = customer)

        return user_tickets.all()