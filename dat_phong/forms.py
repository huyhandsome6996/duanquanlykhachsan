# dat_phong/forms.py
from django import forms
from .models import LichHen

#us-08: task: -Tạo form nhập lịch hẹn
#             -Cấu hình widget ngày và giờ
class LichHenForm(forms.ModelForm):
    class Meta:
        model = LichHen
        fields = ['phong', 'ten_khach', 'so_dien_thoai', 'ngay_den', 'gio_den', 'ghi_chu']
        widgets = {
            'ngay_den': forms.DateInput(attrs={'type': 'date'}),
            'gio_den': forms.TimeInput(attrs={'type': 'time'}),
            'ghi_chu': forms.Textarea(attrs={'rows': 3}),
        }
