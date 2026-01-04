from django.urls import path
from . import views


app_name = 'dat_phong'

urlpatterns = [
    #us-04: task: tạo urls cho tao_dat_phong, danh_sach_dat_phong
    path('tao/', views.tao_dat_phong, name='tao_dat_phong'),
    path('danh-sach/', views.danh_sach_dat_phong, name='danh_sach_dat_phong'),
    #---------------------------------------------
    #us-05: task: tạo urls cho them_dich_vu
    path('them-dich-vu/<int:dat_phong_id>/', views.them_dich_vu, name='them_dich_vu'),
    #---------------------------------------------
    #us-06: task: tạo urls cho check_out
    path('check-out/<int:dat_phong_id>/', views.check_out, name='check_out'), 
    #---------------------------------------------
    #us-08: task: -Tạo urls cho lịch hẹn
    path('lich-hen/', views.lich_hen_list, name='lich_hen_list'),
    path('lich-hen/new/', views.lich_hen_create, name='lich_hen_create'),
    path('lich-hen/<int:pk>/action/<str:action>/', views.lich_hen_action, name='lich_hen_action'),

]
