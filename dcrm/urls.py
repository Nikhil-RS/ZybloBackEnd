from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse





def home(request):
    return HttpResponse("Welcome to the CRM backend API")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('crm.urls')),
    path('', home),  # Root URL handler added
    
]
