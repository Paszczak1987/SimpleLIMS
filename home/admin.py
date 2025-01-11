from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import SystemUser, Client, Manager, Technician
from django.contrib.auth.models import Group
from django.forms import ModelForm

# Formularz do tworzenia użytkownika
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = SystemUser
        fields = ('username', 'email', 'phone_number', 'company')


# Formularz do edycji użytkownika
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = SystemUser
        fields = '__all__'


# Formularz admina dla Technika
class TechnicianAdminForm(ModelForm):
    class Meta:
        model = Technician
        fields = ['username', 'email', 'phone_number', 'company', 'laboratory']  # Dodajemy pole laboratory

# Niestandardowy admin dla SystemUser
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = SystemUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'company', 'is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['username']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number', 'company')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone_number', 'company')}),
    )


# Niestandardowy admin dla Technika
class TechnicianAdmin(CustomUserAdmin):
    form = TechnicianAdminForm  # Używamy niestandardowego formularza
    list_display = CustomUserAdmin.list_display + ['laboratory']  # Dodajemy pole laboratory do listy wyświetlanych
    fieldsets = CustomUserAdmin.fieldsets + (
        ('Technician Info', {'fields': ('laboratory',)}),  # Dodajemy pole laboratory do fieldsets
    )

# Rejestracja w panelu admina
admin.site.register(SystemUser, CustomUserAdmin)
admin.site.register(Client, CustomUserAdmin)  # Rejestracja Client jako CustomUserAdmin
admin.site.register(Manager, CustomUserAdmin)  # Rejestracja Manager jako CustomUserAdmin
admin.site.register(Technician, TechnicianAdmin)  # Rejestracja Technician jako TechnicianAdmin
