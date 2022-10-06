from django.shortcuts import render
from . models import Dosen, Staff, Mahasiswa

# Create your views here.
def prodifh(request):
    judul = ["Ilmu Hukum", "Magister Ilmu Hukum"]
    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'title': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fh.html', konteks)
