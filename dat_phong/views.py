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

        phong.trang_thai = 'dang_thue'
        phong.save()

        return redirect('bao_cao:trang_chu')

    return render(request, 'dat_phong/tao_dat_phong.html', {
        'phong_trong': phong_trong
    })
# us-04: task: Hiển thị danh sách đặt phòng theo trạng thái và thời gian
@staff_member_required
def danh_sach_dat_phong(request):
    danh_sach = DatPhong.objects.select_related('phong') \
        .order_by('-dang_o', '-ngay_nhan')

    return render(request, 'dat_phong/danh_sach_dat_phong.html', {
        'danh_sach': danh_sach
    })

#us-05: task: -Xây dựng chức năng thêm dịch vụ cho đặt phòng
#             -Lưu số lượng dịch vụ sử dụng
@staff_member_required
def them_dich_vu(request, dat_phong_id):
    dat_phong = get_object_or_404(DatPhong, id=dat_phong_id, dang_o=True)
    danh_sach_dich_vu = DichVu.objects.all()

    if request.method == 'POST':
        dich_vu_id = request.POST.get('dich_vu')
        so_luong = int(request.POST.get('so_luong', 1))

        dich_vu = get_object_or_404(DichVu, id=dich_vu_id)

        SuDungDichVu.objects.create(
            dat_phong=dat_phong,
            dich_vu=dich_vu,
            so_luong=so_luong
        )

        return redirect(
            'khach_san:chi_tiet_phong',
            ma_phong=dat_phong.phong.ma_phong
        )

    return render(request, 'dat_phong/them_dich_vu.html', {
        'dat_phong': dat_phong,
        'danh_sach_dich_vu': danh_sach_dich_vu
    })


#us-06: task: -Xây dựng chức năng check-out
#             - Tính số đêm lưu trú
#             -Cập nhật trạng thái phòng
#             -Tạo dữ liệu hóa đơn
@staff_member_required
def check_out(request, dat_phong_id):
    dat_phong = get_object_or_404(DatPhong, id=dat_phong_id, dang_o=True)

    ngay_tra = timezone.now().date()
    so_dem = (ngay_tra - dat_phong.ngay_nhan).days
    if so_dem <= 0:
        so_dem = 1

    gia_mot_dem = dat_phong.phong.loai_phong.gia_mot_dem
    tien_phong = so_dem * gia_mot_dem

    if request.method == 'POST':
        return redirect('hoa_don:chi_tiet', dat_phong.id)

    return render(request, 'dat_phong/checkout.html', {
        'dat_phong': dat_phong,
        'so_dem': so_dem,
        'tien_phong': tien_phong,
    })
