from django.shortcuts import render, get_object_or_404
#from .models import HoaDon
from dat_phong.models import DatPhong
from django.shortcuts import redirect

#us-07: task: -Xem chi tiết hóa đơn (Hiển thị chi tiết hóa đơn của lượt đặt phòng.)
def chi_tiet_hoa_don(request, dat_phong_id):
    pass


#us-07: task: -Xác nhận thanh toán hóa đơn (Cập nhật trạng thái hóa đơn sang đã thanh toán.)
def xac_nhan_thanh_toan(request, dat_phong_id):
    pass