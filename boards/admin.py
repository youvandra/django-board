from django.contrib import admin
from .models import Board,Inventaris,Jenis,Ruang,Level,Pegawai,Peminjaman,Detail

admin.site.register(Board)
admin.site.register(Inventaris)
admin.site.register(Jenis)
admin.site.register(Ruang)
admin.site.register(Level)
admin.site.register(Pegawai)
admin.site.register(Peminjaman)
admin.site.register(Detail)
admin.site.site_title = "Data Inventaris Sarpras SMK"
admin.site.site_header = "Login ke Data Inventaris"