
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home , name='home'),
    path('about_us/', include('about_us.urls')),
    path('meal/', include('meal.urls')),
]
