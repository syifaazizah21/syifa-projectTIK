from django.shortcuts import render
from . models import Dosen, Staff, Mahasiswa

# Create your views here.
def prodifkip(request):
    judul = ["Pendidikan Fisika", "Pendidikan Kimia", "Pendidikan Matematika", "Pendidikan Teknik Vokasional", "Pendidikan IPA", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Sejarah"]
    dosen = Dosen.objects.all()
    staff = Staff.objects.all()
    mahasiswa = Mahasiswa.objects.all()

    konteks = {
        'title': judul,
        'dataDosen': dosen,
        'dataStaff': staff,
        'dataMahasiswa': mahasiswa,
    }
    return render(request, 'fkip.html', konteks)
