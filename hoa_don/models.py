from django.db import models
from dat_phong.models import DatPhong
# Create your models here.
class HoaDon(models.Model):
    dat_phong = models.OneToOneField(
        DatPhong,
        on_delete=models.CASCADE,
        related_name='hoa_don'
    )

    tien_phong = models.PositiveIntegerField(default=0)
    tien_dich_vu = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Hoa don {self.id}"