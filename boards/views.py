from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Inventaris,Jenis,Ruang,Level,Pegawai,Peminjaman,Detail

def Board(request):
    return render (request, 'home.html')

@login_required
def inventaris(request):
    inventariss = Inventaris.objects.all()
    return render(request, 'inventaris.html', {'inventariss': inventariss})

@login_required
def jenis(request):
    jeniss = Jenis.objects.all()
    return render(request, 'jenis.html', {'jeniss': jeniss})

@login_required
def ruang(request):
    ruangs = Ruang.objects.all()
    return render(request, 'ruang.html', {'ruangs': ruangs})

@login_required
def level(request):
    levels = Level.objects.all()
    return render(request, 'level.html', {'levels': levels})

@login_required
def pegawai(request):
    pegawais = Pegawai.objects.all()
    return render(request, 'pegawai.html', {'pegawais': pegawais})

@login_required
def peminjaman(request):
    peminjamans = Peminjaman.objects.all()
    return render(request, 'peminjaman.html', {'peminjamans': peminjamans})

@login_required
def detail(request):
    details = Detail.objects.all()
    return render(request, 'detail.html', {'details': details})



