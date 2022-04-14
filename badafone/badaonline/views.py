from django.shortcuts import render
from .models import Customer
import pandas as pd

# Create your views here.

def customer(request):
	customer_data = pd.DataFrame(Customer.objects.all().values())
	tosend = {
		"data": customer_data
	}
	return render(request, "badaonline/customer.html", tosend)
