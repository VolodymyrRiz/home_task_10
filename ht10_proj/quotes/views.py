
from .utils import get_mongodb
from django.views import View
#from .forms import RegisterForm
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib import messages
#from django.core.paginator import Paginator

# Create your views here.
def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    # per_page = 10
    # paginator = Paginator(list(quotes), per_page)
    # quotes_on_page = paginator.page(page)
    #return render(request, 'quotes/main.html')
    return render(request, 'quotes/index.html', context={'quotes': quotes})
#context={'quotes': quotes_on_page})
    
class RegisterView(View):   
    def quote(self, request):
        
        return render(request,'quotes/quote.html')
    
    def author(self, request):
        
        return render(request,'quotes/author.html')