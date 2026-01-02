from django.shortcuts import render, get_object_or_404, redirect
from .models import Phong
from dat_phong.models import DatPhong

#us-03: task: Hiển thị danh sách phòng
def danh_sach_phong(request):
    pass


#us-03: task: Xem chi tiết phòng
def chi_tiet_phong(request, ma_phong):
    pass



#us-03: task: Cập nhật trạng thái phòng sang đang thuê
def check_in(request, ma_phong):
    pass

#us-03: task: Cập nhật trạng thái phòng về trống
def check_out(request, ma_phong):
    pass 