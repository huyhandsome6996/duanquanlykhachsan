from django.shortcuts import render, get_object_or_404, redirect
from .models import Phong
from dat_phong.models import DatPhong

#us-03: task: Hiển thị danh sách phòng
def danh_sach_phong(request):
    danh_sach_phong = Phong.objects.select_related('loai_phong').all()
    return render(request, 'khach_san/danh_sach_phong.html', {
        'danh_sach_phong': danh_sach_phong
    })



#us-03: task: Xem chi tiết phòng
def chi_tiet_phong(request, ma_phong):
    phong = get_object_or_404(Phong, ma_phong=ma_phong)

    dat_phong_hien_tai = DatPhong.objects.filter(
        phong=phong,
        dang_o=True
    ).first()

    context = {
        'phong': phong,
        'dat_phong_hien_tai': dat_phong_hien_tai
    }

    return render(request, 'khach_san/chi_tiet_phong.html', context)



#us-03: task: Cập nhật trạng thái phòng sang đang thuê
def check_in(request, ma_phong):
    pass

#us-03: task: Cập nhật trạng thái phòng về trống
def check_out(request, ma_phong):
    pass 