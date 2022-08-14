from django.contrib import admin

# Register your models here. daftar model yang telah kita buat
from .models import Model_jenis, Model_barang, Model_jual4, Model_setor1, Model_tarik, Model_nasabah2, Model_pembayaran1

admin.site.register(Model_jenis)
admin.site.register(Model_barang)
admin.site.register(Model_jual4)
admin.site.register(Model_setor1)
admin.site.register(Model_tarik)
admin.site.register(Model_nasabah2)
admin.site.register(Model_pembayaran1)