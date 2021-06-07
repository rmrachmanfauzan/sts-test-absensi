from django.conf.urls import url
from django.urls import path

from . import views

app_name = 'absenapp'
urlpatterns = [
    path('', views.index, name="index"),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('check_in', views.checkin, name='checkin'),
    path('check_out/<int:absen_id>/', views.checkout, name='checkout'),
]
