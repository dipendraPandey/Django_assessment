from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.generics import get_object_or_404
from .serializers import EmployeeSerializer
from ..models import Employee


class EmployeeViewSets(viewsets.ViewSet):
    queryset = Employee.objects.all()

    def list(self, request):
        serializer = EmployeeSerializer(self.queryset, many=True, context={"request": request})
        response_dict = {
            'errors': False,
            'message': "All employee list invoked",
            'data': serializer.data
        }
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {
                'errors': False,
                'message': "Employee Created Successfully",
                'data': serializer.data
            }
        except:
            response_dict = {
                'errors': True,
                'message': "Error Creating Employee",
            }

        return Response(response_dict)

    def update(self, request, pk=None):

        try:
            employee = get_object_or_404(self.queryset, pk=pk)
            serializer = EmployeeSerializer(employee, data=request.data, partial=True, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict = {
                'errors': False,
                'message': "Employee Updated Successfully",
                'data': serializer.data
            }
        except:
            response_dict = {
                'errors': True,
                'message': "Error Updating Employee",
            }
        return Response(response_dict)

    def retrieve(self, request, pk=None):
        try:
            employee = get_object_or_404(self.queryset, pk=pk)
            serializer = EmployeeSerializer(employee, context={"request": request})
            response_dict = {'errors': False,
                             'message': "Employee Details Invoked",
                             'data': serializer.data}

        except:
            response_dict = {"error": True, "message": " Error invoking Employee Details", }

        return Response(response_dict)

    def destroy(self, request, pk=None):
        try:
            employee = get_object_or_404(self.queryset, pk=pk)
            employee.delete()
            response_dict = {
                'errors': False,
                'message': 'Employee Data Deleted Succesfully'
            }

        except:
            response_dict = {
                'error': True,
                'message': "Error Deleting Employee Data"
            }

        return Response(response_dict)


