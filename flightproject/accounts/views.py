from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm , UserUpdateForm , CustomerUpdateForm
from flights.models import Customer , Country

def homepage(request):#get list of flights 'to country' if you click the photo 
        countries = Country.objects.all()
        if request.POST.get('country_id') is not None:
            country_id=int(request.POST.get('country_id'))
            country = Country.objects.filter(id__exact=country_id).first()
            
        return render(request,"homepage.html",{"countries":countries}) 

def register(request):
    if request.method =='POST':
        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account created! you are now logged in')
            return redirect('homepage')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})
    

@login_required
def update_profile(request):#if user already have a customer to its user update, if not create one 
    customer = Customer.objects.filter(user__id__exact = request.user.id).first()

    if request.method == 'POST':
        if (customer == None):
            customer = Customer(user_id = request.user.id)

        customer.first_name = request.POST['first_name']
        customer.last_name = request.POST['last_name']
        customer.address = request.POST['address']
        customer.phone_number = request.POST['phone_number']
        
        user_update_form = UserUpdateForm(request.POST,instance=request.user)
        customer_update_form = CustomerUpdateForm(request.POST, instance=customer)

        if user_update_form.is_valid() and customer_update_form.is_valid():
            user_update_form.save()
            customer_update_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('homepage')

    else:
        if (customer == None):
            customer = Customer(user_id = request.user.id)

        user_update_form = UserUpdateForm(instance=request.user)
        customer_update_form = CustomerUpdateForm(instance=customer)
        

    return render(request ,"profile.html", {'user_update_form': user_update_form,'customer_update_form' : customer_update_form})



