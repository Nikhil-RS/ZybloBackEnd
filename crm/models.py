from django.db import models
from django.utils import timezone
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # You can add more info here if needed

    def __str__(self):
        return self.name



class Manager(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.CharField(max_length=100, blank=True)
    joined_on = models.DateField(default=timezone.now)  # new field with default current date

    def __str__(self):
        return self.full_name

class Staff(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    skills = models.CharField(max_length=200)
    manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True, related_name='staff_members')

    def __str__(self):
        return self.full_name


class Customer(models.Model):
    full_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=20, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    date_of_birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    # You can add a ForeignKey to Manager if needed
    # assigned_manager = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.full_name
