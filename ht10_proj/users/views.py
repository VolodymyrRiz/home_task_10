# from django.views import View
# from .forms import RegisterForm, LoginForm
# from django.contrib import messages
# from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login, logout

# # from django.contrib.auth.decorators import login_required


# class RegisterView(View):
#     template_name = "users/signup.html"
#     form_class = RegisterForm

#     def dispatch(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             return redirect(to="/")
#         return super().dispatch(request, *args, **kwargs)

#     def get(self, request):
#         return render(request, self.template_name, context={"form": self.form_class})

#     def post(self, request):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data["username"]
#             messages.success(request, f"Hello {username}, Your account created successfully")
            
#             return redirect(to="users/login")
#         return render(request, self.template_name, context={"form": form})
    
#     def loginuser(request):
#         if request.user.is_authenticated:            
#             return redirect(to='quotes:main')

#         if request.method == 'POST':
#             user = authenticate(username=request.POST['username'], password=request.POST['password'])
           
#             if user is None:
#                 messages.error(request, 'Username or password didn\'t match')
#                 return redirect(to='users:login')

#             login(request, user)
#             return redirect(to='quotes:index')

#         return render(request, 'users/login.html', context={"form": LoginForm()})
    
from django.views import View
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy


class RegisterView(View):
    template_name = "users/signup.html"
    form_class = RegisterForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('quotes:main')  # Надіслати користувача на головну сторінку, якщо він вже увійшов
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, context={"form": self.form_class})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Hello {username}, Your account created successfully")
            
            return redirect('quotes:main')  # Надіслати користувача на головну сторінку після успішної реєстрації
        return render(request, self.template_name, context={"form": form})

    def register(request):
        if request.method == 'POST':
            form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
        else:
            form = RegisterForm()
        return render(request, 'users/signup.html', {'form': form})

class LoginView(View):
    
    def index(request):
        return render(request, 'index.html')
    
    def get(self, request):
        if request.user.is_authenticated:            
            return redirect('quotes:main')
        return render(request, 'users/login.html', context={"form": LoginForm()})

    def post(self, request):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
       
        if user is None:
            messages.error(request, 'Username or password didn\'t match')
            return redirect('users:login')

        login(request, user)
        return redirect('quotes:main')
    
    def login_view(request):
        if request.method == 'POST':
        # Handle the login process here
            pass
        else:
            form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
    
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('index') 
    
# @login_required
# def logoutuser(request):
#     logout(request)
#     return redirect(to='noteapp:index')

    # def signupuser(request):
    #     if request.user.is_authenticated:
    #         return redirect(to='quotes:index')

    #     if request.method == 'POST':
    #         form = RegisterForm(request.POST)
    #         if form.is_valid():
    #             form.save()
    #             return redirect(to='quotes:index')
    #         else:
    #             return render(request, 'signup.html', context={"form": form})

    #     return render(request, 'signup.html', context={"form": RegisterForm()})


    # def loginuser(request):
    #     if request.user.is_authenticated:
    #         return redirect(to='quotes:index')

    #     if request.method == 'POST':
    #         user = authenticate(
    #             username=request.POST['username'],
    #             password=request.POST['password']
    #         )

    #         if user is None:
    #             messages.error(request, 'Username or password didn\'t match')
    #             return redirect(to='users:login')

    #         login(request, user)
    #         return redirect(to='quotes:index')

    #     return render(request, 'login.html', context={"form": LoginForm()})