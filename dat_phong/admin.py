from django.contrib import admin
from .models import DatPhong
from .models import DichVu
from .models import SuDungDichVu

#us-04: Cấu hình hiển thị DatPhong trong admin
@admin.register(DatPhong)
class DatPhongAdmin(admin.ModelAdmin):
    list_display = (
        'phong',
        'ten_khach',
        'loai_khach',
        'ngay_nhan',
        'ngay_tra',
        'dang_o',
    )

    list_filter = ('loai_khach', 'dang_o')
    search_fields = ('ten_khach',)
