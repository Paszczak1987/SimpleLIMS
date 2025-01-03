from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect, get_object_or_404
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


class ProfileView(View):
    def get_user_group_context(self, user):
        if user.groups.filter(name="Client").exists():
            print(user.building_sites)
            return {
                'profile_type': 'Client',
                'sites': user.building_sites.all(),
            }
        elif user.groups.filter(name="Technician").exists():
            return {
                'profile_type': 'Technician',
                'tasks': 'Lista zadań technicznych',
            }
        elif user.groups.filter(name="Manager").exists():
            return {
                'profile_type': 'Manager',
                'reports': 'Dane zarządcze do przeglądu',
            }
        else:
            return {
                'profile_type': 'Unknown',
                'message': 'Nie przypisano do żadnej grupy.',
            }
    
    def get(self, request):
        user = request.user
        context = {'extra_info': getattr(user, 'extra_info', None)}
        context.update(self.get_user_group_context(user))
        return render(request, 'home/profile.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been logged out successfully.")
        return redirect('home:home_view')
    
    