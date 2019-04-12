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
    id_jenis = models.CharField(max_length=100, unique=True)
    nama_jenis = models.CharField(max_length=100)
    kode_jenis = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=100)

    def __str__(self):
        return self.id_jenis

class Ruang(models.Model):
    id_ruang = models.CharField(max_length=100, unique=True)
    nama_ruang = models.CharField(max_length=100)
    kode_ruang = models.CharField(max_length=100)
    keterangan = models.CharField(max_length=100)

    def __str__(self):
        return self.id_ruang


class Inventaris(models.Model):
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
    id_detail_pinjam = models.CharField(max_length=100, unique=True)
    id_inventaris = models.ForeignKey('Inventaris', on_delete=models.DO_NOTHING, null=True)
    jumlah = models.IntegerField()

    def __str__(self):
        return self.id_detail_pinjam

class Peminjaman(models.Model):
    id_peminjaman = models.CharField(max_length=100, unique=True)
    tanggal_register = models.DateTimeField(auto_now_add=True)
    tanggal_kembali = models.DateTimeField(auto_now_add=False)
    status_peminjaman = models.CharField(max_length=100)
    id_pegawai = models.ForeignKey('Inventaris', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.id_peminjaman

class Pegawai(models.Model):
    id_pegawai = models.CharField(max_length=100, unique=True)
    nama_pegawai = models.CharField(max_length=100)
    nip = models.IntegerField()
    alamat = models.CharField(max_length=255)

    def __str__(self):
        return self.id_pegawai


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.DO_NOTHING,)
    starter = models.ForeignKey(User, related_name='topics',on_delete=models.DO_NOTHING,)
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.subject
    def get_page_count(self):
        count = self.posts.count()
        pages = count / 20
        return math.ceil(pages)

    def has_many_pages(self, count=None):
        if count is None:
            count = self.get_page_count()
        return count > 6

    def get_page_range(self):
        count = self.get_page_count()
        if self.has_many_pages(count):
            return range(1, 5)
        return range(1, count + 1)
    def get_last_ten_posts(self):
        return self.posts.order_by('-created_at')[:10]


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.DO_NOTHING,)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.DO_NOTHING,)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete=models.DO_NOTHING,)
    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)
    def get_message_as_markdown(self):
        return mark_safe(markdown(self.message, safe_mode='escape'))

  
