from django.urls import path
from .views import (
    employee_list_view,
    employee_delete_view,
    employee_detail_view,
    employee_update_view,
    employee_api_view,
)


app_name = "employee"


urlpatterns = [
    path("", employee_list_view, name="employee_list"),
    path("eapi/", employee_api_view, name="eapi"),
    path("<id>/delete", employee_delete_view, name="employee_delete"),
    path("<id>/edit", employee_update_view, name="employee_edit"),
    path("<id>/details", employee_detail_view, name="employee_detail"),
]
