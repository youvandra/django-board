import math
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
from django.utils.html import mark_safe
from markdown import markdown


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
 
    def __str__(self):
        return self.name

class Level(models.Model):
    id_level = models.CharField(max_length=100, unique=True)
    nama_level = models.CharField(max_length=100)

    def __str__(self):
        return self.id_level

class Jenis(models.Model):
    order_jenis = models.IntegerField(default=0, null=True)
    id_jenis = models.CharField(max_length=100, unique=True)
    nama_jenis = models.CharField(max_length=100)
    kode_jenis = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=100)

    def __str__(self):
        return self.id_jenis

class Ruang(models.Model):
    order_ruang = models.IntegerField(default=0, null=True)
    id_ruang = models.CharField(max_length=100, unique=True)
    nama_ruang = models.CharField(max_length=100)
    kode_ruang = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=100)

    def __str__(self):
        return self.id_ruang


class Inventaris(models.Model):
    order_inventaris = models.IntegerField(default=0, null=True)
    id_inventaris = models.CharField(max_length=30, unique=True)
    nama_inventaris = models.CharField(max_length=100)
    kondisi = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=100)
    jumlah = models.IntegerField()
    id_jenis = models.ForeignKey('Jenis', on_delete=models.DO_NOTHING, null=True)
    tanggal_register = models.DateTimeField(auto_now_add=True)
    id_ruang = models.ForeignKey('Ruang', on_delete=models.DO_NOTHING, null=True)
    kode_inventaris = models.CharField(max_length=100)

    def __str__(self):
        return self.id_inventaris

class Detail(models.Model):
    order_detail = models.IntegerField(default=0, null=True)
    id_detail_pinjam = models.CharField(max_length=100, unique=True)
    id_inventaris = models.ForeignKey('Inventaris', on_delete=models.DO_NOTHING, null=True)
    jumlah = models.IntegerField()

    def __str__(self):
        return self.id_detail_pinjam

class Peminjaman(models.Model):
    order_peminjaman = models.IntegerField(default=0, null=True)
    id_peminjaman = models.CharField(max_length=100, unique=True)
    tanggal_register = models.DateTimeField(auto_now_add=True)
    tanggal_kembali = models.DateTimeField()
    status_peminjaman = models.CharField(max_length=100)
    id_pegawai = models.ForeignKey('Inventaris', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.id_peminjaman

class Pegawai(models.Model):
    order_pegawai = models.IntegerField(default=0, null=True)
    id_pegawai = models.CharField(max_length=100, unique=True)
    nama_pegawai = models.CharField(max_length=100)
    nip = models.IntegerField()
    alamat = models.CharField(max_length=255)

    def __str__(self):
        return self.id_pegawai
