from .utils import get_mongodb
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import TagForm, QuoteForm
from .models import Tag, Quote


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
    tags = Tag.objects.filter(user=request.user).all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save(commit=False)
            new_quote.user = request.user
            new_quote.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'), user=request.user)
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quotes:main')
        else:
            return render(request, 'quotes/quote.html', {"tags": tags, 'form': form})

    return render(request, 'quotes/quote.html', {"tags": tags, 'form': QuoteForm()})

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