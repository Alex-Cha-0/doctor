from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from geopy.distance import geodesic as GD
from geopy import distance


class Doctor(models.Model):
    name = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name='Начальная Широта геолокация врача',
                                   default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name='Начальная Долгота геолокация врача',
                                    default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name.get_full_name()


class Orders(models.Model):
    doc_name = models.ForeignKey(Doctor, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Назначен врач')
    latitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name='Широта геолокация пациента')
    longitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name='Долгота геолокация пациента')
    timestamp = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    patient_name = models.CharField(max_length=50)
    is_active = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return f'"{self.patient_name}" - {self.text[:50]}'

    def get_distance(self):
        if self.doc_name:
            patient_geo = (self.latitude, self.longitude)
            doctor_geo = (self.doc_name.latitude, self.doc_name.longitude)
            return float('{:.1f}'.format(distance.distance(doctor_geo, patient_geo).km))


class Route(models.Model):
    doc_name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name='По маршрута Широта геолокация врача')
    longitude = models.DecimalField(max_digits=10, decimal_places=7,
                                    verbose_name='По маршруту Долгота геолокация врача')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order}'

    def get_curent_time_in_work(self):
        return timezone.now() - self.timestamp

    def get_distance(self):
        if self.doc_name:
            patient_geo = (self.order.latitude, self.order.longitude)
            doctor_geo = (self.latitude, self.longitude)
            return float('{:.1f}'.format(distance.distance(doctor_geo, patient_geo).km))
