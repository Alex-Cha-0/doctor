from django.contrib import admin
from app_doctor.models import *


class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'latitude', 'longitude', 'timestamp',)


class OrdersAdmin(admin.ModelAdmin):
    list_display = (
        'doc_name', 'patient_name', 'text', 'is_active', 'timestamp', 'latitude', 'longitude')


class RouteAdmin(admin.ModelAdmin):
    list_display = (
        'doc_name', 'order', 'latitude', 'longitude', 'timestamp',)


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Orders, OrdersAdmin)
admin.site.register(Route, RouteAdmin)
