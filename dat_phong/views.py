from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from datetime import datetime

from khach_san.models import Phong
from .models import DatPhong, SuDungDichVu, DichVu, LichHen
from hoa_don.models import HoaDon

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse



@staff_member_required
def tao_dat_phong(request):
    phong_trong = Phong.objects.filter(trang_thai='trong')

    if request.method == 'POST':
        phong_id = request.POST.get('phong')
        phong = get_object_or_404(Phong, id=phong_id)

        if phong.trang_thai != 'trong':
            return render(request, 'dat_phong/tao_dat_phong.html', {
                'phong_trong': phong_trong,
                'error': 'Phòng này hiện không còn trống.'
            })

        ten_khach = request.POST.get('ten_khach')
        loai_khach = request.POST.get('loai_khach')
        ngay_nhan = datetime.strptime(request.POST.get('ngay_nhan'), '%Y-%m-%d').date()
        ngay_tra_du_kien = datetime.strptime(request.POST.get('ngay_tra_du_kien'), '%Y-%m-%d').date()

        DatPhong.objects.create(
            phong=phong,
            ten_khach=ten_khach,
            loai_khach=loai_khach,
            ngay_nhan=ngay_nhan,
            ngay_tra_du_kien=ngay_tra_du_kien,
            dang_o=True
        )

        return redirect('bao_cao:trang_chu')

    return render(request, 'dat_phong/tao_dat_phong.html', {
        'phong_trong': phong_trong
    })
# us-04: task: Hiển thị danh sách đặt phòng theo trạng thái và thời gian
@staff_member_required
def danh_sach_dat_phong(request):
    pass


