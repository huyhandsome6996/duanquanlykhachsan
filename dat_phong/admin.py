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

#us-05: task: Quản lý dịch vụ và dịch vụ đã sử dụng trong admin
@admin.register(DichVu)
class DichVuAdmin(admin.ModelAdmin):
    list_display = ('ten_dich_vu', 'gia', 'don_vi')
@admin.register(SuDungDichVu)
class SuDungDichVuAdmin(admin.ModelAdmin):
    list_display = ('dat_phong', 'dich_vu', 'so_luong', 'thoi_diem')


#us-08: task: -Quản lý lịch hẹn trong admin
#             - Lọc theo trạng thái và ngày
from django.contrib import admin
from .models import LichHen

@admin.register(LichHen)
class LichHenAdmin(admin.ModelAdmin):
    list_display = ('ten_khach', 'phong', 'ngay_den', 'gio_den', 'trang_thai', 'created_by', 'ngay_tao')
    list_filter = ('trang_thai', 'ngay_den')
    search_fields = ('ten_khach', 'so_dien_thoai', 'phong__ma_phong')