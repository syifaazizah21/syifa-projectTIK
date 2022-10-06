from django.shortcuts import render
from . models import Dosen, Staff, Mahasiswa

# Create your views here.
def prodipasca(request):
    judul = ["Doktor Pendidikan", "Doktor Ilmu Pertanian", "Doktor Ilmu Akuntansi", "Magister Ilmu Hukum", "Magister Manajemen", "Magister Teknik Kimia"]
    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'title': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'pascasarjana.html', konteks)
