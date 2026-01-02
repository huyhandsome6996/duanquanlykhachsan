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
    pass

# us-04: task: Hiển thị danh sách đặt phòng theo trạng thái và thời gian
@staff_member_required
def danh_sach_dat_phong(request):
    pass


