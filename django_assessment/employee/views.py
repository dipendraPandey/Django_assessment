from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms


# views for employee


def employee_api_view(request):
    return render(request, "employee/knockoutApi.html", {})


def employee_list_view(request):
    employee_list = models.Employee.objects.all()
    form = forms.EmployeeCreationForm
    contents = {"employee_list": employee_list, "form": form}
    template = "employee/employee_list.html"

    if request.method == "POST":
        print("hello i am inside the post request")
        form = forms.EmployeeCreationForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()

            return redirect("employee:employee_list")
        else:

            contents = {"form": form}
            return render(request, template, contents)

    return render(request, template, contents)


def employee_delete_view(request, id):
    employee = get_object_or_404(models.Employee, id=id)
    employee.delete()
    return redirect("employee:employee_list")


def employee_update_view(request, id):
    employee = get_object_or_404(models.Employee, id=id)
    form = forms.EmployeeCreationForm(instance=employee)
    contents = {"employee_details": employee, "form": form}
    template_name = "employee/employee_update.html"
    if request.method == "POST":
        form = forms.EmployeeCreationForm(
            request.POST, request.FILES, instance=employee
        )
        if form.is_valid():
            employee.save()
            return redirect("employee:employee_list")
        else:

            contents = {"form": form}
    return render(request, template_name, contents)


def employee_detail_view(request, id):
    employee = get_object_or_404(models.Employee, id=id)
    contents = {"employee_details": employee}
    template_name = "employee/employee_detail.html"
    return render(request, template_name, contents)
