from django.shortcuts import render
from . models import Dosen, Staff, Mahasiswa

# Create your views here.
def prodift(request):
    judul = ["Teknik Industri", "Teknik Sipil", "Teknik Elektro", "Teknik Mesin", "Teknik Metalurgi"]
    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'title': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'ft.html', konteks)
