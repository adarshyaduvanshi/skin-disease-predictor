

from django.contrib import admin
from django.urls import path, include

from health_ai.views import upload_form_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('health_ai.urls')),

    
    path('', upload_form_view, name='home'),
]