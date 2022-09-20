from rest_framework import routers
from crud_app.viewsets import EmployeeViewset
from crud_app.serializers import EmployeeSerializer

router = routers.DefaultRouter()
router.register(r'employee', EmployeeViewset)