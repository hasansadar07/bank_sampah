from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Model_jenis(models.Model):
	jenis_sampah	= models.CharField(max_length = 1200)
	satuan	=models.CharField(max_length = 12)
	harga	=models.CharField(max_length = 25)
	gambar	=models.ImageField(upload_to ='Berkas/', null=True)	
	keterangan	=models.CharField(max_length = 12000)	

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.jenis_sampah)

class Model_pembayaran1(models.Model):	
	jenis_sampah	= models.CharField(max_length = 1200)
	nama_nasabah	=models.CharField(max_length = 25)
	nama_barang	=models.CharField(max_length = 12)
	harga	=models.CharField(max_length = 25)
	jumlah	=models.CharField(max_length = 25)
	total	=models.CharField(max_length = 12000)	
	bayar	=models.CharField(max_length = 25)
	kembalian	=models.CharField(max_length = 25)
	tanggal	=models.CharField(max_length = 25)
	bulan	=models.CharField(max_length = 25)
	tahun	=models.CharField(max_length = 25)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.jenis_sampah)

class Model_barang(models.Model):
	kode_barang	= models.CharField(max_length = 12)
	nama_barang	=models.CharField(max_length = 1200)
	jenis_sampah	=models.CharField(max_length = 2500)
	stock	=models.CharField(max_length = 25)
	keterangan	=models.CharField(max_length = 12000)	
	tanggal	=models.DateTimeField(max_length = 25)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):	
		return "{}.{}".format(self.id, self.nama_barang)		

class Model_jual4(models.Model):
	kode_jual	= models.CharField(max_length = 12)
	kode_barang = models.CharField(max_length = 12)
	nama_barang	=models.CharField(max_length = 1200)
	jenis_sampah	=models.CharField(max_length = 2500)
	harga	=models.CharField(max_length = 25)
	jumlah	=models.CharField(max_length = 12)	
	total	=models.CharField(max_length = 12)	
	tanggal	=models.CharField(max_length = 25)
	bulan	=models.CharField(max_length = 25)
	tahun	=models.CharField(max_length = 25)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.jenis_sampah)				

class Model_setor1(models.Model):
	kode_setor	= models.CharField(max_length = 12)
	nama_setor	=models.CharField(max_length = 1200)
	id_nasabah = models.CharField(max_length = 12)
	nama_nasabah	=models.CharField(max_length = 1200)
	telp	=models.CharField(max_length = 12)
	alamat	=models.CharField(max_length = 2500)
	jenis_sampah	=models.CharField(max_length = 1200)	
	berat	=models.CharField(max_length = 12)	
	harga	=models.CharField(max_length = 12)	
	total	=models.CharField(max_length = 12)		
	tanggal	=models.CharField(max_length = 25)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_setor)

class Model_tarik(models.Model):
	kode_tarik	= models.CharField(max_length = 12)
	nama_tarik	=models.CharField(max_length = 1200)
	id_nasabah = models.CharField(max_length = 12)
	nama_nasabah	=models.CharField(max_length = 1200)
	telp	=models.CharField(max_length = 12)
	alamat	=models.CharField(max_length = 2500)
	jenis_sampah	=models.CharField(max_length = 1200)	
	jumlah_tari	=models.CharField(max_length = 12)	
	berat	=models.CharField(max_length = 12)	
	total	=models.CharField(max_length = 12)		
	tanggal	=models.DateTimeField(max_length = 25)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_tarik)

class Model_nasabah2(models.Model):
	id_nasabah = models.CharField(max_length = 12)
	nama_nasabah	=models.CharField(max_length = 1200)
	telp	=models.CharField(max_length = 12)
	alamat	=models.CharField(max_length = 2500)
	password	=models.CharField(max_length = 1200)
	tanggal	=models.CharField(max_length = 25)
	bulan	=models.CharField(max_length = 25)
	tahun	=models.CharField(max_length = 25)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.nama_nasabah)		