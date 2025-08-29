from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('managers/', views.manager_list, name='manager-list'),
    path('departments/', views.department_list, name='department-list'),
    path('customers/', views.customer_list, name='customer-list'),  # fixed spelling and lowercase
    path('staff/', views.staff_list, name='staff-list'),            # lowercase
    path('customers/count/', views.customers_count, name='customers-count'),
    path('staff/count/', views.staff_count, name='staff-count'),
    path('managers/count/', views.managers_count, name='managers-count'),
    path('departments/count/', views.departments_count, name='departments-count'),
]
