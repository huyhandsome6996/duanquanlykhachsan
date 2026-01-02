from django.core.management.base import BaseCommand
from django.utils import timezone
from dat_phong.models import DatPhong


class Command(BaseCommand):
    
    help = "Tự động trả phòng khi đến ngày trả dự kiến"

    def handle(self, *args, **kwargs):
        pass