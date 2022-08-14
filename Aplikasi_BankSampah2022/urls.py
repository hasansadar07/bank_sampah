from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from Aplikasi_BankSampah2022 import settings
from django.urls import path
# from django.contrib.auth import views
from django.contrib import admin
from . import views

from .views import W_jenis, index, HomeView, LogoutView, Data_jenis, Tambah_jenis, Hapus_jenis, Edit_jenis, Data_barang, Edit_barang, Tambah_barang, Hapus_barang, Data_nasabah, Tambah_nasabah, Edit_nasabah, Hapus_nasabah, Data_setor, Tambah_setor, Hapus_setor, Edit_setor, laporan_pembayaran, proses_setor, Data_tarik, Tambah_tarik, Edit_tarik, Hapus_tarik, Proses_tarik, Data_penjualan, Tambah_penjualan, Edit_penjualan, Hapus_penjualan, Halaman_menu, LP_barang, LP_nasabah, LP_penjualan, LP_setor, LP_tarik, WEBSITE, Login_WEBSITE, W_setor, W_tarik, Data_pembayaran, Tambah_pembayaran, Hapus_pembayaran, nota_pembayaran, LP_nasabah_bulan, LP_nasabah_tahun, LP_penjualan_tahun, LP_penjualan_bulan, laporan_pembayaran_bulan1, laporan_pembayaran_tahun1, laporan_pembayaran_tanggal, LP_nasabah_tanggal, LP_penjualan_tanggal
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(r'^$',index, name="index"),
    url(r'^Home/$', HomeView, name="Home"),
    url(r'^logout/$',LogoutView, name="logout"),

    # data jenis
    url(r'^jenis/$', Data_jenis, name="jenis"),
    url(r'^tambah_jenis/$', Tambah_jenis, name="tambah_jenis"),
    url(r'^hapus_jenis/(?P<hapus_j>[0-9]+)$',Hapus_jenis, name="hapus_jenis"),
    url(r'^edit_jenis/(?P<id_j>[0-9]+)$',Edit_jenis, name="edit_jenis"),

    # data barang
    url(r'^barang/$', Data_barang, name="barang"),
    url(r'^tambah_barang/$', Tambah_barang, name="tambah_barang"),
    url(r'^hapus_barang/(?P<hapus_b>[0-9]+)$',Hapus_barang, name="hapus_barang"),
    url(r'^edit_barang/(?P<id_b>[0-9]+)$',Edit_barang, name="edit_barang"),

    # data nasabah
    url(r'^nasabah/$', Data_nasabah, name="nasabah"),
    url(r'^tambah_nasabah/$', Tambah_nasabah, name="tambah_nasabah"),
    url(r'^hapus_nasabah/(?P<hapus_n>[0-9]+)$',Hapus_nasabah, name="hapus_nasabah"),
    url(r'^edit_nasabah/(?P<id_n>[0-9]+)$',Edit_nasabah, name="edit_nasabah"),

    # data setor
    url(r'^setor/$', Data_setor, name="setor"),
    url(r'^tambah_setor/$', Tambah_setor, name="tambah_setor"),
    url(r'^proses_data1/$',proses_setor, name="proses_data1"),
    url(r'^hapus_setor/(?P<hapus_s>[0-9]+)$',Hapus_setor, name="hapus_setor"),
    url(r'^edit_setor/(?P<id_s>[0-9]+)$',Edit_setor, name="edit_setor"),

    # data tarik
    url(r'^tarik/$', Data_tarik, name="tarik"),
    url(r'^tambah_tarik/$', Tambah_tarik, name="tambah_tarik"),
    url(r'^proses_tarik/(?P<id_pro>[0-9]+)$',Proses_tarik, name="proses_tarik"),
    url(r'^hapus_tarik/(?P<hapus_t>[0-9]+)$',Hapus_tarik, name="hapus_tarik"),
    url(r'^edit_tarik/(?P<id_t>[0-9]+)$',Edit_tarik, name="edit_tarik"),

    # data pejualan
    url(r'^jual/$', Data_penjualan, name="jual"),
    url(r'^tambah_jual/$', Tambah_penjualan, name="tambah_jual"),
    url(r'^hapus_jual/(?P<hapus_pj>[0-9]+)$',Hapus_penjualan, name="hapus_jual"),
    url(r'^edit_jual/(?P<id_jual>[0-9]+)$',Edit_penjualan, name="edit_jual"),

    # pembayaran
    url(r'^pembayaran/$', Data_pembayaran, name="pembayaran"),
    url(r'^tambah_pembayaran/$', Tambah_pembayaran, name="tambah_pembayaran"),
    url(r'^hapus_pembayaran/(?P<hapus_pb>[0-9]+)$',Hapus_pembayaran, name="hapus_pembayaran"),
    url(r'^nota_pembayaran/$', nota_pembayaran, name="nota_pembayaran"),
    
    

    # halaman menu laporan
    url(r'^menu_lp/$', Halaman_menu, name="menu_lp"),
    url(r'^lp_barang/$', LP_barang, name="lp_barang"),
    url(r'^lp_nasabah/$', LP_nasabah, name="lp_nasabah"),
    url(r'^lp_nasabah_bulan/$', LP_nasabah_bulan, name="lp_nasabah_bulan"),
    url(r'^lp_nasabah_tahun/$', LP_nasabah_tahun, name="lp_nasabah_tahun"),
    url(r'^LP_nasabah_tanggal/$', LP_nasabah_tanggal, name="LP_nasabah_tanggal"),
    # ---------------------------------------
    url(r'^lp_penjualan/$', LP_penjualan, name="lp_penjualan"),
    url(r'^lp_penjualan_bulan/$', LP_penjualan_bulan, name="lp_penjualan_bulan"),
    url(r'^lp_penjualan_tahun/$', LP_penjualan_tahun, name="lp_penjualan_tahun"),
    url(r'^LP_penjualan_tanggal/$', LP_penjualan_tanggal, name="LP_penjualan_tanggal"),
    # -------------------
    url(r'^lp_setor/$', LP_setor, name="lp_setor"),
    url(r'^lp_tarik/$', LP_tarik, name="lp_tarik"),


    # website bank sampah
    url(r'^website/$', WEBSITE, name="website"),
    url(r'^login_website/$', Login_WEBSITE, name="login_website"),
    url(r'^W_setor/$', W_setor, name="W_setor"),
    url(r'^W_tarik/$', W_tarik, name="W_tarik"),
    url(r'^W_jenis/$', W_jenis, name="W_jenis"),
    url(r'^laporan_pembayaran/$', laporan_pembayaran, name="laporan_pembayaran"),
    url(r'^laporan_pembayaran_bulan/$', laporan_pembayaran_bulan1, name="laporan_pembayaran_bulan"),
    url(r'^laporan_pembayaran_tahun/$', laporan_pembayaran_tahun1, name="laporan_pembayaran_tahun"),
    url(r'^laporan_pembayaran_tanggal/$', laporan_pembayaran_tanggal, name="laporan_pembayaran_tanggal"),
    
    

    path('admin/', admin.site.urls),
]

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)