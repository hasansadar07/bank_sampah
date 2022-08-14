from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Model_jenis, Model_barang, Model_jual4, Model_setor1, Model_tarik, Model_nasabah2, Model_pembayaran1
import hashlib


def index(request):
	context = {
	'page_title':'Login',
	}
	#print(request.user)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Home')
		else:
			return redirect('index')

	return render(request, 'login.html',  context)

def HomeView(request):	
	context = {
	'page_title':'Home'
	}
	return render(request, 'home.html',  context)

def LogoutView(request):
	context = {
	'page_title':'logout',
	}
	if request.method == "POST":
		if request.POST["logout"] == "Submit":	
			logout(request)

		return redirect('index')

	return render(request, 'logout.html',  context)	


	# data jenis
def Data_jenis(request):
	data = Model_jenis.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_jenis/tabel.html',  context)	

def Tambah_jenis(request):
	if request.method == 'POST':
		Model_jenis.objects.create(
			jenis_sampah = request.POST['jenis_sampah'],
			satuan = request.POST['satuan'],
			harga = request.POST['harga'],			
			gambar = request.FILES['gambar'],			
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/jenis/")		
	context = {	
	'Tambah_jenis':'Tambah_jenis',
	}
	return render(request, 'Master_data/data_jenis/tambah.html',  context)	

def Hapus_jenis(request, hapus_j):
	Model_jenis.objects.filter(id=hapus_j).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('jenis')

def Edit_jenis(request, id_j):		
	edit_data = Model_jenis.objects.get(id=id_j)
	if request.method == 'POST':		
			edit_data.jenis_sampah = request.POST.get('jenis_sampah')
			edit_data.satuan = request.POST.get('satuan')
			edit_data.harga = request.POST.get('harga')
			edit_data.gambar = request.FILES.get('gambar')
			edit_data.keterangan = request.POST.get('keterangan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('jenis')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_jenis/edit.html',  context)		

# data barang sampah
def Data_barang(request):
	data = Model_barang.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/Data_barang/tabel.html',  context)	

def Tambah_barang(request):
	select_data = Model_jenis.objects.all()
	kode_data = Model_barang.objects.count()
	if request.method == 'POST':
		Model_barang.objects.create(
			kode_barang = request.POST['kode_barang'],
			nama_barang = request.POST['nama_barang'],
			jenis_sampah = request.POST['jenis_sampah'],			
			stock = request.POST['stock'],			
			keterangan = request.POST['keterangan'],
			tanggal = request.POST['tanggal'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/barang/")		
	context = {	
	'Tambah_jenis':'Tambah_jenis',
	'select_data': select_data,
	'kode_data': kode_data,
	}
	return render(request, 'Master_data/Data_barang/tambah.html',  context)	

def Hapus_barang(request, hapus_b):
	Model_barang.objects.filter(id=hapus_b).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('barang')

def Edit_barang(request, id_b):	
	select_data = Model_jenis.objects.all()	
	edit_data = Model_barang.objects.get(id=id_b)
	if request.method == 'POST':		
			edit_data.kode_barang = request.POST.get('kode_barang')
			edit_data.nama_barang = request.POST.get('nama_barang')
			edit_data.jenis_sampah = request.POST.get('jenis_sampah')
			edit_data.stock = request.POST.get('stock')
			edit_data.keterangan = request.POST.get('keterangan')
			edit_data.tanggal = request.POST.get('tanggal')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('barang')

	context = {'edit_data': edit_data, 'select_data': select_data}
	return render(request, 'Master_data/Data_barang/edit.html',  context)		

# data nasabah
def Data_nasabah(request):
	data = Model_nasabah2.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_nasabah/tabel.html',  context)	

def Tambah_nasabah(request):
	kode_data = Model_nasabah2.objects.count()
	if request.method == 'POST':
		Model_nasabah2.objects.create(
			id_nasabah = request.POST['id_nasabah'],
			nama_nasabah = request.POST['nama_nasabah'],
			telp = request.POST['telp'],			
			alamat = request.POST['alamat'],			
			password = request.POST['password'],
			tanggal = request.POST['tanggal'],
			bulan = request.POST['bulan'],
			tahun = request.POST['tahun'],			
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/nasabah/")		
	context = {	
	'Tambah_nasabah':'Tambah_nasabah',
	'kode_data': kode_data,
	}
	return render(request, 'Master_data/data_nasabah/tambah.html',  context)	

def Hapus_nasabah(request, hapus_n):
	Model_nasabah2.objects.filter(id=hapus_n).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('nasabah')

def Edit_nasabah(request, id_n):		
	edit_data = Model_nasabah2.objects.get(id=id_n)
	if request.method == 'POST':		
			edit_data.id_nasabah = request.POST.get('id_nasabah')
			edit_data.nama_nasabah = request.POST.get('nama_nasabah')
			edit_data.telp = request.POST.get('telp')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.password = request.POST.get('password')
			edit_data.tanggal = request.POST.get('tanggal')
			edit_data.bulan = request.POST.get('bulan')
			edit_data.tahun = request.POST.get('tahun')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('nasabah')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_nasabah/edit.html',  context)		

# data setor atau penimbangan
def Data_setor(request):
	data = Model_setor1.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_setor/tabel.html',  context)	

def Tambah_setor(request):
	data = Model_nasabah2.objects.all()
	select_jenis = Model_jenis.objects.all()
	context = {	
	'Tambah_setor':'Tambah_setor',
	'data': data,
	'select_jenis': select_jenis,
	}
	return render(request, 'Master_data/data_setor/tambah.html',  context)	

def proses_setor(request):	
	kode_data = Model_setor1.objects.count()	
	select_jenis = Model_jenis.objects.all()
	# cari data
	if 'cari_data' in request.GET:
		cari_data=request.GET['cari_data']
		data = Model_jenis.objects.filter(jenis_sampah=cari_data)
	else:
		data = Model_jenis.objects.filter(jenis_sampah=None)	
	# tampil jenis
	for tampil in data:
		jenis_sampah1 = tampil.jenis_sampah
		harga1= tampil.harga
	# end cari
	# cari nasabah
	if 'cari_id_nasabah' in request.GET:
		cari_data_n=request.GET['cari_id_nasabah']
		data_n = Model_nasabah2.objects.filter(id=cari_data_n)
	else:
		data_n = Model_nasabah2.objects.filter(id=None)	

	for tampil in data_n:
		id_nasabah =tampil.id_nasabah
		nama_nasabah = tampil.nama_nasabah
		telp = tampil.telp
		alamat = tampil.alamat

	if request.method == 'POST':
		Model_setor1.objects.create(
			kode_setor = request.POST['kode_setor'],
			nama_setor = request.POST['nama_setor'],
			id_nasabah = request.POST['id_nasabah'],			
			nama_nasabah = request.POST['nama_nasabah'],			
			telp = request.POST['telp'],
			alamat = request.POST['alamat'],
			jenis_sampah = request.POST['jenis_sampah'],
			berat = request.POST['berat'],
			harga = request.POST['harga'],
			total = request.POST['total'],
			tanggal = request.POST['tanggal'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/setor/")		
	context = {	
	'Tambah_setor':'Tambah_setor',
	'kode_data': kode_data,
	# 'proses_data': proses_data,
	'select_jenis': select_jenis,
	'jenis_sampah1': jenis_sampah1,
	'harga1': harga1,
	'id_nasabah': id_nasabah,
	'nama_nasabah': nama_nasabah,
	'telp': telp,
	'alamat': alamat,
	# jenis
	}
	return render(request, 'Master_data/data_setor/proses_data.html',  context)		

def Hapus_setor(request, hapus_s):
	Model_setor1.objects.filter(id=hapus_s).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('setor')

def Edit_setor(request, id_s):		
	edit_data = Model_setor1.objects.get(id=id_s)
	select_jenis = Model_jenis.objects.all()
	if request.method == 'POST':		
			edit_data.kode_setor = request.POST.get('kode_setor')
			edit_data.nama_setor = request.POST.get('nama_setor')
			edit_data.id_nasabah = request.POST.get('id_nasabah')
			edit_data.nama_nasabah = request.POST.get('nama_nasabah')
			edit_data.telp = request.POST.get('telp')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.jenis_sampah = request.POST.get('jenis_sampah')
			edit_data.berat = request.POST.get('berat')
			edit_data.harga = request.POST.get('harga')
			edit_data.total = request.POST.get('total')
			edit_data.tanggal = request.POST.get('tanggal')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('setor')

	context = {'edit_data': edit_data, 'select_jenis': select_jenis,}
	return render(request, 'Master_data/data_setor/edit.html',  context)		

# data tarik atau jemput
def Data_tarik(request):
	data = Model_tarik.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_tarik/tabel.html',  context)	

def Tambah_tarik(request):
	data_nasabah = Model_nasabah2.objects.all()
	context = {	
	'Tambah_tarik':'Tambah_tarik',
	'data_nasabah': 'data_nasabah1',
	}
	return render(request, 'Master_data/data_tarik/tambah.html',  context)	

def Proses_tarik(request, id_pro):
	kode_data = Model_tarik.objects.count()
	proses_data = Model_nasabah2.objects.get(id=id_pro)
	select_jenis = Model_jenis.objects.all()
	if request.method == 'POST':
		Model_tarik.objects.create(
			kode_tarik = request.POST['kode_tarik'],
			nama_tarik = request.POST['nama_tarik'],
			id_nasabah = request.POST['id_nasabah'],			
			nama_nasabah = request.POST['nama_nasabah'],			
			telp = request.POST['telp'],			
			alamat = request.POST['alamat'],
			jenis_sampah = request.POST['jenis_sampah'],
			jumlah_tari = request.POST['jumlah_tari'],
			berat = request.POST['berat'],
			total = request.POST['total'],
			tanggal = request.POST['tanggal'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/tarik/")		
	context = {	
	'Tambah_tarik':'Tambah_tarik',
	'kode_data': kode_data,
	'proses_data': proses_data,
	'select_jenis': select_jenis
	}
	return render(request, 'Master_data/data_tarik/proses_data.html',  context)		

def Hapus_tarik(request, hapus_t):
	Model_tarik.objects.filter(id=hapus_t).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('tarik')

def Edit_tarik(request, id_t):
	edit_data = Model_tarik.objects.get(id=id_t)
	if request.method == 'POST':		
			edit_data.kode_tarik = request.POST.get('kode_tarik')
			edit_data.nama_tarik = request.POST.get('nama_tarik')
			edit_data.id_nasabah = request.POST.get('id_nasabah')
			edit_data.nama_nasabah = request.POST.get('nama_nasabah')
			edit_data.telp = request.POST.get('telp')
			edit_data.alamat = request.POST.get('alamat')
			edit_data.jenis_sampah = request.POST.get('jenis_sampah')
			edit_data.jumlah_tari = request.POST.get('jumlah_tari')
			edit_data.berat = request.POST.get('berat')
			edit_data.total = request.POST.get('total')
			edit_data.tanggal = request.POST.get('tanggal')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('tarik')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_tarik/edit.html',  context)		

	# data penjualan
def Data_penjualan(request):
	data = Model_jual4.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_penjualan/tabel.html',  context)	

def Tambah_penjualan(request):
	select_jenis = Model_jenis.objects.all()
	kode_data = Model_jual4.objects.count()
	if 'cari_data' in request.GET:
		cari_data=request.GET['cari_data']
		data = Model_jenis.objects.filter(jenis_sampah=cari_data)		
	else:
		data = Model_jenis.objects.filter(jenis_sampah=None)

	# for tampil in data:
	# 	jenis_sampah= tampil.jenis_sampah

	if 'cari_data' in request.GET:
		cari_data=request.GET['cari_data']
		data_b = Model_barang.objects.filter(jenis_sampah=cari_data)		
	else:
		data_b = Model_barang.objects.filter(jenis_sampah=None)
	

	if request.method == 'POST':
		Model_jual4.objects.create(
			kode_jual = request.POST['kode_jual'],
			kode_barang = request.POST['kode_barang'],
			nama_barang = request.POST['nama_barang'],
			jenis_sampah = request.POST['jenis_sampah'],
			harga = request.POST['harga'],
			jumlah = request.POST['jumlah'],
			total = request.POST['total'],
			tanggal = request.POST['tanggal'],
			bulan = request.POST['bulan'],
			tahun = request.POST['tahun'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/jual/")		
	context = {	
	'Tambah_jual':'Tambah_jual',
	'select_jenis': select_jenis,
	'data': data,
	'data_b': data_b,
	'kode_data': kode_data,
	# 'jenis_sampah': jenis_sampah,
	# 'harga': harga,
	}
	return render(request, 'Master_data/data_penjualan/tambah.html',  context)	

def Hapus_penjualan(request, hapus_pj):
	Model_jual4.objects.filter(id=hapus_pj).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('jual')

def Edit_penjualan(request, id_jual):
	edit_data = Model_jual4.objects.get(id=id_jual)
	if request.method == 'POST':		
			edit_data.kode_jual = request.POST.get('kode_jual')
			edit_data.kode_barang = request.POST.get('kode_barang')
			edit_data.nama_barang = request.POST.get('nama_barang')
			edit_data.jenis_sampah = request.POST.get('jenis_sampah')
			edit_data.harga = request.POST.get('harga')
			edit_data.jumlah = request.POST.get('jumlah')
			edit_data.total = request.POST.get('total')
			edit_data.tanggal = request.POST.get('tanggal')
			edit_data.bulan = request.POST.get('bulan')
			edit_data.tahun = request.POST.get('tahun')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..')
			return redirect('jual')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_penjualan/edit.html',  context)			

	# halaman menu laporan
def Halaman_menu(request):	
	context = {
	'page_title':'Halaman_menu'
	}
	return render(request, 'Master_data/laporan/menu.html',  context)	

def LP_barang(request):
	data = Model_barang.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_barang.html',  context)	

def LP_nasabah(request):
	data = Model_nasabah2.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_nasabah.html',  context)		
# bulan
def LP_nasabah_bulan(request):
	if 'bulan' in request.GET:
		bulan=request.GET['bulan']
		data = Model_nasabah2.objects.filter(bulan=bulan)		
	else:
		data = Model_nasabah2.objects.filter(bulan=None)

	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_nasabah_bulan.html',  context)		
# tahun
def LP_nasabah_tahun(request):
	if 'tahun' in request.GET:
		tahun=request.GET['tahun']
		data = Model_nasabah2.objects.filter(tahun=tahun)		
	else:
		data = Model_nasabah2.objects.filter(tahun=None)

	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_nasabah_tahun.html',  context)		
# tanggal
def LP_nasabah_tanggal(request):
	if 'tanggal_dari' in request.GET:
		tanggal_dari=request.GET['tanggal_dari']
		tanggal_sampai=request.GET['tanggal_sampai']
		data = Model_nasabah2.objects.filter(tanggal=tanggal_dari).filter(tanggal=tanggal_sampai)		
	else:
		data = Model_nasabah2.objects.filter(tanggal=tanggal_dari).filter(tanggal=tanggal_sampai)

	

	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_nasabah_bulan.html',  context)
# -------------------------------------------

def LP_penjualan(request):
	data = Model_jual4.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_penjualan.html',  context)			
def LP_penjualan_bulan(request):
	if 'bulan' in request.GET:
		bulan=request.GET['bulan']
		data = Model_jual4.objects.filter(bulan=bulan)		
	else:
		data = Model_jual4.objects.filter(bulan=None)

	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_penjualan_bulan.html',  context)		
# tahun
def LP_penjualan_tahun(request):
	if 'tahun' in request.GET:
		tahun=request.GET['tahun']
		data = Model_jual4.objects.filter(tahun=tahun)		
	else:
		data = Model_jual4.objects.filter(tahun=None)

	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_penjualan_tahun.html',  context)		
# tangagl
def LP_penjualan_tanggal(request):
	if 'tanggal_dari1' in request.GET:
		tanggal_dari1=request.GET['tanggal_dari1']
		data = Model_jual4.objects.filter(tanggal=tanggal_dari1)		
	else:
		data = Model_jual4.objects.all()

	if 'tanggal_sampai1' in request.GET:
		tanggal_sampai1=request.GET['tanggal_sampai1']
		data = Model_jual4.objects.filter(tanggal=tanggal_sampai1)		
	else:
		data = Model_jual4.objects.all()

	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_penjualan_bulan.html',  context)
	# ---------------

def LP_setor(request):
	data = Model_setor1.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_setor.html',  context)				

def LP_tarik(request):
	data = Model_tarik.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_tarik.html',  context)					

	# website bank sampah
def WEBSITE(request):
	data = Model_jenis.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'WEBSITE/index.html',  context)						

def Login_WEBSITE(request):
	if 'id_nasabah' in request.GET:
		c_id_nasabah=request.GET['id_nasabah']
		data_n = Model_nasabah2.objects.filter(id_nasabah=c_id_nasabah)		
	else:
		data_n = Model_nasabah2.objects.filter(id_nasabah=None)

	if 'password' in request.GET:
		cari_data=request.GET['password']
		data = Model_nasabah2.objects.filter(password=cari_data)		
	else:
		data = Model_nasabah2.objects.filter(password=None)
	context = {	
	'data': data,
	'data_n': data_n
	}
	return render(request, 'WEBSITE/Master_data/home.html',  context)							

def W_setor(request):
	data = Model_setor1.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'WEBSITE/Master_data/data/setor.html',  context)

def W_tarik(request):
	data = Model_tarik.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'WEBSITE/Master_data/data/tarik.html',  context)
def W_jenis(request):
    data = Model_jenis.objects.all()
    context = {	
	'data': data,
	}
    return render(request, 'WEBSITE/Master_data/data/jenis.html',  context)
    

# pembayaran
def Data_pembayaran(request):
	data = Model_pembayaran1.objects.all()
	context = {	
	'data': data,
	}
	return render(request, 'Master_data/data_pembayaran/tabel.html',  context)

def laporan_pembayaran(request):
    data = Model_pembayaran1.objects.all()
    context = {	
	'data': data,
	}
    return render(request, 'Master_data/data_pembayaran/nota.html',  context)	

def laporan_pembayaran_bulan1(request):
	if 'bulan' in request.GET:
		bulan=request.GET['bulan']
		data = Model_pembayaran1.objects.filter(bulan=bulan)		
	else:
		data = Model_pembayaran1.objects.filter(bulan=None)

	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_setor_bulan.html',  context)		
# tahun
def laporan_pembayaran_tahun1(request):
	if 'tahun' in request.GET:
		tahun=request.GET['tahun']
		data = Model_pembayaran1.objects.filter(tahun=tahun)		
	else:
		data = Model_pembayaran1.objects.filter(tahun=None)

	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_setor_tahun.html',  context)
# tanggal
def laporan_pembayaran_tanggal(request):
	if 'tanggal_dari' in request.GET:
		tahun=request.GET['tanggal_dari']
		data = Model_pembayaran1.objects.filter(tanggal=tahun)		
	else:
		data = Model_pembayaran1.objects.filter(tanggal=None)

	if 'tanggal_sampai' in request.GET:
		tahun=request.GET['tanggal_sampai']
		data = Model_pembayaran1.objects.filter(tanggal=tahun)		
	else:
		data = Model_pembayaran1.objects.filter(tanggal=None)

	context = {	
	'data': data,
	}
	return render(request, 'Master_data/laporan/lp_setor_tanggal.html',  context)



def Tambah_pembayaran(request):
	# proses pembayaran jual kenasabah
	if 'cari_data' in request.GET:
		cari_data=request.GET['cari_data']
		data = Model_jual4.objects.filter(jenis_sampah=cari_data)
	else:
		data = Model_jual4.objects.filter(jenis_sampah=None)	
	# tampil jenis
	for tampil in data:
		jenis_sampah = tampil.jenis_sampah
		harga= tampil.harga
		nama_barang= tampil.nama_barang
		jumlah= tampil.jumlah
		total= tampil.total

	if request.method == 'POST':
		Model_pembayaran1.objects.create(
			jenis_sampah = request.POST['jenis_sampah'],
			nama_nasabah = request.POST['nama_nasabah'],
			nama_barang = request.POST['nama_barang'],			
			harga = request.POST['harga'],			
			jumlah = request.POST['jumlah'],	
			total = request.POST['total'],
			bayar = request.POST['bayar'],
			kembalian = request.POST['kembalian'],
			tanggal = request.POST['tanggal'],
			bulan = request.POST['bulan'],
			tahun = request.POST['tahun'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..')
		return HttpResponseRedirect("/pembayaran/")		
	context = {	
	'tambah':'tambah',
	'jenis_sampah': jenis_sampah,
	'harga': harga,
	'nama_barang': nama_barang,
	'jumlah': jumlah,
	'total': total
	}
	return render(request, 'Master_data/data_pembayaran/tambah.html',  context)	
def nota_pembayaran(request):
	if 'cari_data' in request.GET:
		cari_data=request.GET['cari_data']
		data = Model_pembayaran1.objects.filter(id=cari_data)
	else:
		data = Model_pembayaran1.objects.filter(id=None)	
	context = {	
	'data':data,
	}

	return render(request, 'Master_data/data_pembayaran/nota.html',  context)	
def Hapus_pembayaran(request, hapus_pb):
	Model_pembayaran1.objects.filter(id=hapus_pb).delete()
	messages.info(request, 'Data Berhasil Di Hapus..')
	return redirect('pembayaran')