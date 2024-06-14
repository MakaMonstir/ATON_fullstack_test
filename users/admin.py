from django.contrib import admin
from .models import User, Client

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'full_name')
    list_filter = ('is_staff', 'is_active')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'last_name', 'first_name', 'middle_name', 'birth_date', 'inn', 'responsible_person', 'status')
    search_fields = ('account_number', 'last_name', 'first_name', 'inn')
    list_filter = ('status', 'responsible_person')
