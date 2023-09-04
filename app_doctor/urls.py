from django.contrib import admin
from django.urls import path

from app_doctor.views import *

app_name = 'app_doctor'

urlpatterns = [
    path('', OrderList.as_view(), name='home'),
    path('doctor/location/<int:pk>', DoctorLocationAPIView.as_view(), name='doctor_location'),
    path('order/create/', OrdersApiCreate.as_view(), name='order_create'),
    path('orders/list/', OrderList.as_view(), name='orders_list'),
    path('doctors/list/', DoctorList.as_view(), name='doctors_list'),
    path('orders/update/<int:pk>', OrderUpdateView.as_view(), name='order_update'),
    path('doctors/update/<int:pk>', DoctorUpdateView.as_view(), name='doctor_update'),
    path('route/add/<int:order_id>/<int:name>', RouteAdd.as_view(), name='add_route'),
    path('route/update/<int:order_id>/<int:name>', RouteUpdate.as_view(), name='route_update'),
    path('route/detail/<int:pk>', RouteDetail.as_view(), name='route_detail'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]
