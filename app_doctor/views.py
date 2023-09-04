from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from rest_framework.response import Response
from django.contrib import messages
from .forms import *
from .models import *


class DoctorLocationAPIView(UpdateView):
    template_name = 'doctor.html'
    form_class = DoctorForm
    success_url = reverse_lazy(
        'app_doctor:home')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Doctor.objects.get(name=id)


class OrdersApiCreate(CreateView):
    template_name = 'order.html'
    form_class = OrdersClientForm
    success_url = reverse_lazy(
        'app_doctor:home')


class OrderList(ListView):
    model = Orders
    template_name = 'table.html'
    context_object_name = 'orders'
    queryset = Orders.objects.order_by('-timestamp')


class OrderUpdateView(UpdateView):
    template_name = 'order_update.html'
    form_class = OrdersUpdateForm
    success_url = reverse_lazy(
        'app_doctor:home')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Orders.objects.get(pk=id)


class DoctorUpdateView(UpdateView):
    template_name = 'doctor_update.html'
    form_class = DoctorForm
    success_url = reverse_lazy(
        'app_doctor:doctors_list')

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Doctor.objects.get(pk=id)


class RouteAdd(CreateView):
    template_name = 'route_add.html'
    form_class = RouteForm
    success_url = reverse_lazy(
        'app_doctor:home')

    def get_initial(self):
        initial = super(RouteAdd, self).get_initial()
        order_id = self.kwargs["order_id"]
        name = self.kwargs["name"]
        initial['doc_name'] = name
        initial['order'] = order_id
        return initial


class DoctorList(ListView):
    model = Doctor
    template_name = 'doctors_info.html'
    context_object_name = 'doctors'
    queryset = Doctor.objects.all()


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app_doctor:home')
    else:
        form = UserLoginForm()

    return render(request, 'login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('app_doctor:login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Регистрация успешна')
            return redirect('app_doctor:home')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {"form": form})


class RouteDetail(DetailView):
    model = Orders
    template_name = 'route.html'
    context_object_name = 'order'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RouteDetail, self).get_context_data(**kwargs)
        order_id = self.kwargs.get('pk', None)
        context['route'] = Route.objects.get(order=order_id)
        return context


class RouteUpdate(UpdateView):
    model = Route
    template_name = 'route_update.html'
    form_class = RouteFormUpdate

    def get_object(self, **kwargs):
        order_id = self.kwargs["order_id"]
        name = self.kwargs["name"]
        return Route.objects.get(order=order_id, doc_name=name)

    def get_success_url(self):
        order_id = self.kwargs["order_id"]
        return reverse("app_doctor:route_detail", kwargs={"pk": order_id})

