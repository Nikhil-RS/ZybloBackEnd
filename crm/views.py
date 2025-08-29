from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Manager, Department, Staff, Customer
from .serializers import ManagerSerializer, DepartmentSerializer, StaffSerializer, CustomerSerializer

# Manager list and create
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manager_list(request):
    if request.method == 'GET':
        managers = Manager.objects.all()
        serializer = ManagerSerializer(managers, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = ManagerSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Manager created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Department list and create
@api_view(['GET'])
def department_list(request):
    departments = Department.objects.all()
    serializer = DepartmentSerializer(departments, many=True)
    return Response(serializer.data) 
# Staff list and create
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def staff_list(request):
    if request.method == 'GET':
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Staff created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Customer list and create
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def customer_list(request):
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Customer created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customers_count(request):
    count = Customer.objects.count()
    return Response({'count': count})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def staff_count(request):
    count = Staff.objects.count()
    return Response({'count': count})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def managers_count(request):
    count = Manager.objects.count()
    return Response({'count': count})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def departments_count(request):
    count = Department.objects.count()
    return Response({'count': count})