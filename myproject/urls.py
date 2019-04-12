from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from accounts import views as accounts_views
from boards import views

urlpatterns = [
    url(r'^$', views.Board, name='home'),
    url(r'^signup/$', accounts_views.signup, name='signup'),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^inventaris/$', views.inventaris, name='inventaris'),
    url(r'^jenis/$', views.jenis, name='jenis'),
    url(r'^ruang/$', views.ruang, name='ruang'),
    url(r'^level/$', views.level, name='level'),
    url(r'^pegawai/$', views.pegawai, name='pegawai'),
    url(r'^peminjaman/$', views.peminjaman, name='peminjaman'),
    url(r'^detail/$', views.detail, name='detail'),
    url(r'^admin/', admin.site.urls),
url(r'^settings/password/$', auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
    name='password_change'),
url(r'^settings/password/done/$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
    name='password_change_done'),
url(r'^settings/account/$', accounts_views.UserUpdateView.as_view(), name='my_account'),
]
