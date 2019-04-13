from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Inventaris,Jenis,Ruang,Level,Pegawai,Peminjaman,Detail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def Board(request):
    count_inventaris = Inventaris.objects.filter(order_inventaris=0).count()
    count_jenis = Jenis.objects.filter(order_jenis=0).count()
    count_ruang = Ruang.objects.filter(order_ruang=0).count()
    count_pegawai = Pegawai.objects.filter(order_pegawai=0).count()
    count_peminjaman = Peminjaman.objects.filter(order_peminjaman=0).count()
    count_detail = Detail.objects.filter(order_detail=0).count()
    context = {'count_inventaris': count_inventaris,
               'count_jenis' : count_jenis,
               'count_ruang' : count_ruang,
               'count_pegawai' : count_pegawai,
               'count_peminjaman' : count_peminjaman,
               'count_detail' : count_detail}
    return render (request, 'home.html', context)

@login_required
def inventaris(request):
    inventariss = Inventaris.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(inventariss,4)
    try:
        inventaris = paginator.page(page)
    except PageNotAnInteger:
        inventaris = paginator.page(1)
    except EmptyPage:
        inventaris = paginator.page(paginator.num_pages)
    inven = {'inventaris' : inventaris }
    return render(request, 'inventaris.html', inven)

@login_required
def jenis(request):
    jeniss = Jenis.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(jeniss, 4)
    try:
        jenis = paginator.page(page)
    except PageNotAnInteger:
        jenis = paginator.page(1)
    except EmptyPage:
        jenis= paginator.page(paginator.num_pages)
    jns = {'jenis': jenis}
    return render(request, 'jenis.html', jns)

@login_required
def ruang(request):
    ruangs = Ruang.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(ruangs, 4)
    try:
        ruang = paginator.page(page)
    except PageNotAnInteger:
        ruang = paginator.page(1)
    except EmptyPage:
        ruang = paginator.page(paginator.num_pages)
    rag = {'ruang': ruang}
    return render(request, 'ruang.html', rag)

@login_required
def level(request):
    levels = Level.objects.all()
    return render(request, 'level.html', {'levels': levels})

@login_required
def pegawai(request):
    pegawais = Pegawai.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(pegawais, 4)
    try:
        pegawai = paginator.page(page)
    except PageNotAnInteger:
        pegawai = paginator.page(1)
    except EmptyPage:
        pegawai = paginator.page(paginator.num_pages)
    pgw = {'pegawai': pegawai}
    return render(request, 'pegawai.html', pgw)

@login_required
def peminjaman(request):
    peminjamans = Peminjaman.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(peminjamans, 4)
    try:
        peminjaman = paginator.page(page)
    except PageNotAnInteger:
        peminjaman = paginator.page(1)
    except EmptyPage:
        peminjaman = paginator.page(paginator.num_pages)
    pjm = {'peminjaman': peminjaman}
    return render(request, 'peminjaman.html', pjm)

@login_required
def detail(request):
    details = Detail.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(details, 4)
    try:
        detail = paginator.page(page)
    except PageNotAnInteger:
        detail = paginator.page(1)
    except EmptyPage:
        detail = paginator.page(paginator.num_pages)
    dtl = {'detail': detail}
    return render(request, 'detail.html', dtl)



