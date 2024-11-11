from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments,Employees
from EmployeeApp.serializers import DepartmentSerializer,EmployeeSerializer

from django.core.files.storage import default_storage

# Create your views here.

def home(request):
    return  render(request,'home.html')



@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        if id > 0:
            # Fetch a single department by ID
            try:
                department = Departments.objects.get(DepartmentId=id)
                department_serializer = DepartmentSerializer(department)
                return JsonResponse(department_serializer.data, safe=False)
            except Departments.DoesNotExist:
                return JsonResponse({"error": "Department not found"}, status=404)
        else:
            # Fetch all departments
            departments = Departments.objects.all()
            departments_serializer = DepartmentSerializer(departments, many=True)
            return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        try:
            department = Departments.objects.get(DepartmentId=department_data['DepartmentId'])
            department_serializer = DepartmentSerializer(department, data=department_data)
            if department_serializer.is_valid():
                department_serializer.save()
                return JsonResponse("Updated Successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        except Departments.DoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=404)

    elif request.method == 'DELETE':
        try:
            department = Departments.objects.get(DepartmentId=id)
            department.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Departments.DoesNotExist:
            return JsonResponse({"error": "Department not found"}, status=404)


@csrf_exempt


@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        if id > 0:
            # Fetch a single employee by ID
            try:
                employee = Employees.objects.get(EmployeeId=id)
                employee_serializer = EmployeeSerializer(employee)
                return JsonResponse(employee_serializer.data, safe=False)
            except Employees.DoesNotExist:
                return JsonResponse({"error": "Employee not found"}, status=404)
        else:
            # Fetch all employees
            employees = Employees.objects.all()
            employees_serializer = EmployeeSerializer(employees, many=True)
            return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        try:
            employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
            employee_serializer = EmployeeSerializer(employee, data=employee_data)
            if employee_serializer.is_valid():
                employee_serializer.save()
                return JsonResponse("Updated Successfully", safe=False)
            return JsonResponse("Failed to Update", safe=False)
        except Employees.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=404)

    elif request.method == 'DELETE':
        try:
            employee = Employees.objects.get(EmployeeId=id)
            employee.delete()
            return JsonResponse("Deleted Successfully", safe=False)
        except Employees.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=404)



@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)