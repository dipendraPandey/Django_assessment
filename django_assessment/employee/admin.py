from django.contrib import admin
from .models import Employee


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address', 'email', 'phone_number')
    search_fields = ('full_name', 'phone_number')


admin.site.register(Employee, EmployeeAdmin)
