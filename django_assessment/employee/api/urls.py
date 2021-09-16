
from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('employee', views.EmployeeViewSets, basename='employee')

urlpatterns = [
    path('api/', include(router.urls)),
]