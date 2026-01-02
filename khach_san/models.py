from django.db import models

class LoaiPhong(models.Model):
    ten_loai = models.CharField(max_length=100)
    gia_mot_dem = models.PositiveIntegerField(
        verbose_name="Giá / đêm (VND)"
    )
    def __str__(self):
        return self.ten_loai
