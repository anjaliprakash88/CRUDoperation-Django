from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_form'),
    path('list/', views.employee_list, name='employee_list'),
    path('<int:id>', views.employee_update, name='employee_update'),
    path('delete/<int:id>', views.employee_delete, name='employee_delete'),
]
