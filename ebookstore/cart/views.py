from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import HttpResponse

# Create your views here.
class CartView(ListView):
	def get(self, request):
		return HttpResponse("cart")