from rest_framework import serializers
from .models import Customer, Department, Manager, Staff

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name')

class ManagerSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)  # for displaying department object
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department', write_only=True
    )

    class Meta:
        model = Manager
        fields = (
            'id',
            'full_name',
            'email',
            'phone',
            'department',      # read-only object
            'department_id',   # write-only field
            'team',
            'joined_on',
        )

class StaffSerializer(serializers.ModelSerializer):
    manager = ManagerSerializer(read_only=True)   # For displaying manager object
    manager_id = serializers.PrimaryKeyRelatedField(
        queryset=Manager.objects.all(), source='manager', write_only=True
    )

    class Meta:
        model = Staff
        fields = ['id', 'full_name', 'email', 'phone', 'skills', 'manager', 'manager_id']

class CustomerSerializer(serializers.ModelSerializer):
    # Optionally, if including assigned_manager field:
    # assigned_manager = ManagerSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = (
            'id',
            'full_name',
            'gender',
            'date_of_birth',
            'phone',
            'email',
            # 'assigned_manager',
        )
