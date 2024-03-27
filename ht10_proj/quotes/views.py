from .utils import get_mongodb
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import TagForm, QuoteForm
from .models import Tag, Quote

import json
from bson.objectid import ObjectId
from pymongo import MongoClient
from pymongo.server_api import ServerApi


client = MongoClient('mongodb://localhost:27017') 
db = client.hw

def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    
    return render(request, 'quotes/index.html', context={'quotes': quotes})

@login_required
def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            tag = form.save(commit=False)
            tag.user = request.user
            tag.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/tag.html', {'form': form})

    return render(request, 'quotes/tag.html', {'form': TagForm()})

@login_required
def quote(request):
    client = MongoClient('mongodb://localhost:27017') 
    db = client['hw']
    quotes_collection = db['quotes']
    
    form = QuoteForm(request.POST)
    if form.is_valid():
        quote_data = form.cleaned_data  # Get the cleaned data from the form
        # Insert the document into the 'quotes' collection
        quotes_collection.insert_one({
            'quote': quote_data['quote'],
            'tags': quote_data['tags'],
            'author': quote_data['author'],
        })
        # No need to call save on the collection, as insert_one already saves the document
        return redirect(to='quotes:main')
    else:
        print(form.errors)
    # If the form is not valid, you might want to handle the error or display the form again
    # For now, we'll just return to the main view
    return render(request, 'quotes/quote.html', {'form': QuoteForm()})
    # else:
    #     #     return render(request, 'quotes/quote.html', {"tags": tags, 'form': form})

    # #return render(request, 'quotes/quote.html', {"tags": tags, 'form': QuoteForm()})
    #     return render(request, 'quotes/quote.html', {'form': QuoteForm()})

@login_required
def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id, user=request.user)
    return render(request, 'quotes/detail.html', {"quote": quote})

@login_required
def set_done(request, quote_id):
    Quote.objects.filter(pk=quote_id, user=request.user).update(done=True)
    return redirect(to='quotes:main')


@login_required
def delete_quote(request, quote_id):
    Quote.objects.get(pk=quote_id, user=request.user).delete()
    return redirect(to='quotes:main')

@login_required
def author(request, author_id):
    Quote.objects.get(pk=author_id, user=request.user).delete()
    return redirect(to='quotes:main')

# for quote_ in quotes:
    #     quot = Quote(quote=quote_.get("quote"),
    #                     tags=quote_.get("tags"),
    #                     author=quote_.get('author'),
    #                     )
          
    #     quot.save()   


    # if request.method == 'POST':
    #     form = QuoteForm(request.POST)
    #     if form.is_valid():
    #         # quote = form.save(commit=False)
    #         # quote.user = request.user
    #         # quote.save()
    #         # choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'), user=request.user)
    #         # for tag in choice_tags.iterator():
    #         #     quote.tags.add(tag)
    #         # author = form.save(commit=False)
    #         # author.user = request.user
    #         # author.save()
    #            # choice_author = Author.objects.filter(name__in=request.POST.getlist('author'), user=request.user)             
    
    #         for quote in quotes:
    
    # #author = db.authors.find_one({'fullname': quote['author']})    
    
    # #if author:
    #             db.quotes.insert_one({
    #                 'quote': quote['quote'],
    #                 'tags': quote['tags'],
    #                 'author': quote['author'],
    #             })
            



# from .utils import get_mongodb
# from django.views import View
# #from .forms import RegisterForm
# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# from django.contrib import messages
# #from django.core.paginator import Paginator

# # Create your views here.
# def main(request, page=1):
#     db = get_mongodb()
#     quotes = db.quotes.find()
#     # per_page = 10
#     # paginator = Paginator(list(quotes), per_page)
#     # quotes_on_page = paginator.page(page)
#     #return render(request, 'quotes/main.html')
#     return render(request, 'quotes/index.html', context={'quotes': quotes})
# #context={'quotes': quotes_on_page})
    
# class RegisterView(View):   
#     def quote(self, request):
        
#         return render(request,'quotes/quote.html')
    
#     def author(self, request):
        
#         return render(request,'quotes/author.html')
    
#     def tag(self, request):
        
#         return render(request,'quotes/tag.html')

# def quote(request):
#     client = MongoClient('mongodb://localhost:27017') 
#     db = client['hw']
#     quotes_collection = db['quotes']
    
#     form = QuoteForm(request.POST)
#     if form.is_valid():
#         # rest of your code
#     else:
#         print(form.errors)