from django.contrib import admin
from .models import Phong, LoaiPhong


@admin.register(LoaiPhong)
class LoaiPhongAdmin(admin.ModelAdmin):
    list_display = ('ten_loai','gia_mot_dem')
