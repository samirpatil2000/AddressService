from django.shortcuts import render, redirect
from .forms import AddressForm
# Create your views here.



def create_address(request):
    address_form = AddressForm()
    if request.method == "POST":
        address_form = AddressForm(request.POST or None)
        if address_form.is_valid():
            address_form.save()
            return redirect("address")

    context = {
        "form": address_form
    }
    return render(request, template_name='address/create_address.html', context=context)


