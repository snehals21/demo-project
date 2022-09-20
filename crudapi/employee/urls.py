from django.urls import path, include
from .views import EmployeeViewsets
# from .router import router

urlpatterns = [
    path('', EmployeeViewsets.as_view({'get':'list'})),
    path('create', EmployeeViewsets.as_view({'post':'create'})),
]
