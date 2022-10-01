from django.shortcuts import render

# Create your views here.
def prodifkip(request):
    judul = ["Pendidikan Non Formal", "Pendidikan Bahasa Indonesia", "Pendidikan Bahasa Inggris", "Pendidikan Biologi", "Pendidikan Matematika", "Pendidikan Guru Sekolah Dasar", "Pendidikan Guru PAUD", "Bimbingan dan Konseling"]

    konteks = {
        'title': judul,
    }
    return render(request, 'fkip.html', konteks)
