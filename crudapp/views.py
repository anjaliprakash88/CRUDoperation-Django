from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponse
from django.views.generic import View


def employee_list(request):
    context = Employee.objects.all()
    return render(request, 'employee_list.html', {"context": context})


def employee_form(request):
    if request.method == 'GET':
        form = EmployeeForm()
        return render(request, 'employee_form.html', {'form': form})
    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('employee_list')


def employee_update(request, id=0):
    if request.method == "POST":
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance=employee)
            if form.is_valid():
                form.save()
                return redirect('employee_list')
    else:
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})


def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')




