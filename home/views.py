from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.utils.html import format_html
from django.views import View


# Create your views here.
class HomeView(View):
    def get(self, request):
        return render(request, template_name='home/home.html')

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        self.add_bootstrap_classes(form)
        return render(request, 'home/login.html', {'form': form})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        self.add_bootstrap_classes(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home:home_view')
        messages.error(request, "Invalid username or password.")
        return render(request, 'home/login.html', {'form': form})
    
    def add_bootstrap_classes(self, form):
        for field_name, field in form.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',
                'placeholder': format_html('Enter your {}', field.label.lower())
            })


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect('home:home_view')
    
    