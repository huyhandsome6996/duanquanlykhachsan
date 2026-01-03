from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime

from khach_san.models import Phong
from .models import DatPhong, SuDungDichVu, DichVu #,LichHen
# from hoa_don.models import HoaDon

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse



@staff_member_required
def tao_dat_phong(request):
    pass

# us-04: task: Hiển thị danh sách đặt phòng theo trạng thái và thời gian
@staff_member_required
def danh_sach_dat_phong(request):
    pass

#us-05: task: -Xây dựng chức năng thêm dịch vụ cho đặt phòng
#             -Lưu số lượng dịch vụ sử dụng
@staff_member_required
def them_dich_vu(request, dat_phong_id):
    dat_phong = get_object_or_404(DatPhong, id=dat_phong_id, dang_o=True)
    danh_sach_dich_vu = DichVu.objects.all()

    if request.method == 'POST':
        dich_vu_id = request.POST.get('dich_vu')
        dich_vu = get_object_or_404(DichVu, id=dich_vu_id)

        SuDungDichVu.objects.create(
            dat_phong=dat_phong,
            dich_vu=dich_vu
        )

        return redirect(
            'khach_san:chi_tiet_phong',
            ma_phong=dat_phong.phong.ma_phong
        )

    return render(request, 'dat_phong/them_dich_vu.html', {
        'dat_phong': dat_phong,
        'danh_sach_dich_vu': danh_sach_dich_vu
    })


