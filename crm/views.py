from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Manager, Department, Staff, Customer
from .serializers import ManagerSerializer, DepartmentSerializer, StaffSerializer, CustomerSerializer
from django.db.models import Q



def apply_filters(queryset, request):
    q = request.GET.get('q', None)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)

    # text search
    if q:
        queryset = queryset.filter(
            Q(full_name__icontains=q) |
            Q(email__icontains=q) |
            Q(phone__icontains=q)
        )

    
    if start_date and end_date:
        queryset = queryset.filter(added_on__range=[start_date, end_date])

    return queryset



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def manager_list(request):
    if request.method == 'GET':
        managers = apply_filters(Manager.objects.all(), request)
        serializer = ManagerSerializer(managers, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Manager created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def department_list(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Department created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def staff_list(request):
    if request.method == 'GET':
        staff = apply_filters(Staff.objects.all(), request)
        serializer = StaffSerializer(staff, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Staff created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def customer_list(request):
    if request.method == 'GET':
        customers = apply_filters(Customer.objects.all(), request)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Customer created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def customers_count(request):
    return Response({'count': Customer.objects.count()})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def staff_count(request):
    return Response({'count': Staff.objects.count()})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def managers_count(request):
    return Response({'count': Manager.objects.count()})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def departments_count(request):
    return Response({'count': Department.objects.count()})
