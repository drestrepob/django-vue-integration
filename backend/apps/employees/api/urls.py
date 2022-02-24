from rest_framework import routers

from apps.employees.api.viewsets import DepartmentViewSet, EmployeeViewSet


router = routers.SimpleRouter()
router.register("departments", DepartmentViewSet)
router.register("employees", EmployeeViewSet)

urlpatterns = router.urls
