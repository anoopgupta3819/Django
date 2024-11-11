from django.urls import path
from EmployeeApp import views

urlpatterns = [
    path('department', views.departmentApi),              # Matches /department
    path('department/<int:id>', views.departmentApi),
    path('employee',views.employeeApi),
    path('department/<int:id>',views.employeeApi),     # Matches /department/1, /department/2, etc.
]
